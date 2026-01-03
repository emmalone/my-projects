#!/usr/bin/env python3
"""
Project Scanner - Auto-discover all projects in PycharmProjects

Scans /Users/mark/PycharmProjects for:
- Git repositories
- Project metadata (README, package.json, requirements.txt)
- Markdown documentation files
- Tech stack information
- Current status

Generates:
- projects/{project-name}.md - Project profiles
- inventory.json - Complete project inventory
"""

import json
import os
import subprocess
from pathlib import Path
from datetime import datetime
import re

class ProjectScanner:
    def __init__(self, base_path="/Users/mark/PycharmProjects"):
        self.base_path = Path(base_path)
        self.projects = []
        self.all_markdown_files = []

    def scan_all(self):
        """Scan all projects in PycharmProjects"""
        print(f"🔍 Scanning {self.base_path} for projects...")

        # Get all subdirectories
        for item in self.base_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Skip my-projects itself, template, and problematic projects
                if item.name in ['my-projects', '.claude', 'klm-hugo-lab']:
                    continue

                project_info = self.scan_project(item)
                if project_info:
                    self.projects.append(project_info)
                    print(f"✅ Found: {item.name}")

        print(f"\n📊 Total projects found: {len(self.projects)}")
        print(f"📄 Total markdown files: {len(self.all_markdown_files)}")

        return {
            'projects': self.projects,
            'markdown_files': self.all_markdown_files,
            'scan_date': datetime.now().isoformat()
        }

    def scan_project(self, project_path):
        """Scan individual project for metadata"""
        project = {
            'name': project_path.name,
            'path': str(project_path),
            'is_git_repo': (project_path / '.git').exists(),
            'readme': None,
            'tech_stack': self.detect_tech_stack(project_path),
            'markdown_files': [],
            'size_mb': None,
            'last_modified': None
        }

        # Check for README
        for readme_name in ['README.md', 'readme.md', 'README', 'CLAUDE.md', 'claude.md']:
            readme_path = project_path / readme_name
            if readme_path.exists():
                project['readme'] = str(readme_path)
                project['readme_content'] = self.read_file_safe(readme_path, max_chars=500)
                break

        # Find all markdown files
        markdown_files = list(project_path.rglob('*.md'))
        for md_file in markdown_files:
            # Skip files in node_modules, venv, .git, themes, archetypes, etc.
            if any(part in md_file.parts for part in ['node_modules', 'venv', '.git', 'dist', 'build', 'themes', 'archetypes']):
                continue

            md_info = {
                'project': project_path.name,
                'file_path': str(md_file),
                'relative_path': str(md_file.relative_to(project_path)),
                'name': md_file.name,
                'size': md_file.stat().st_size,
                'modified': datetime.fromtimestamp(md_file.stat().st_mtime).isoformat(),
                'summary': self.extract_summary(md_file)
            }

            project['markdown_files'].append(md_info)
            self.all_markdown_files.append(md_info)

        # Get Git info if it's a repo
        if project['is_git_repo']:
            project['git'] = self.get_git_info(project_path)

        # Get project size
        try:
            size = sum(f.stat().st_size for f in project_path.rglob('*') if f.is_file())
            project['size_mb'] = round(size / (1024 * 1024), 2)
        except:
            pass

        return project

    def detect_tech_stack(self, project_path):
        """Detect technologies used in project"""
        tech_stack = []

        # Python
        if (project_path / 'requirements.txt').exists():
            tech_stack.append('Python')
        if (project_path / 'setup.py').exists():
            tech_stack.append('Python Package')
        if (project_path / 'pyproject.toml').exists():
            tech_stack.append('Python (Poetry)')

        # Node.js
        if (project_path / 'package.json').exists():
            tech_stack.append('Node.js')
            try:
                with open(project_path / 'package.json') as f:
                    pkg = json.load(f)
                    deps = list(pkg.get('dependencies', {}).keys())
                    if 'react' in deps:
                        tech_stack.append('React')
                    if 'vue' in deps:
                        tech_stack.append('Vue')
                    if 'express' in deps:
                        tech_stack.append('Express')
            except:
                pass

        # Hugo
        if (project_path / 'hugo.toml').exists() or (project_path / 'config.toml').exists():
            tech_stack.append('Hugo')

        # Docker
        if (project_path / 'Dockerfile').exists():
            tech_stack.append('Docker')
        if (project_path / 'docker-compose.yml').exists():
            tech_stack.append('Docker Compose')

        # AWS
        if (project_path / 'lambda-auth.js').exists():
            tech_stack.append('AWS Lambda')
        if any(f.name.startswith('cloudfront') for f in project_path.glob('*')):
            tech_stack.append('AWS CloudFront')

        # GitHub Actions
        if (project_path / '.github' / 'workflows').exists():
            tech_stack.append('GitHub Actions')

        return tech_stack

    def get_git_info(self, project_path):
        """Get Git repository information"""
        git_info = {}

        try:
            # Current branch
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            git_info['branch'] = result.stdout.strip()

            # Remote URL
            result = subprocess.run(
                ['git', 'remote', 'get-url', 'origin'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            remote_url = result.stdout.strip()
            if remote_url:
                # Convert git@ URL to https://
                if remote_url.startswith('git@github.com:'):
                    remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
                if remote_url.endswith('.git'):
                    remote_url = remote_url[:-4]
                git_info['remote_url'] = remote_url

            # Last commit
            result = subprocess.run(
                ['git', 'log', '-1', '--format=%H|%an|%ae|%ar|%s'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            if result.stdout:
                hash, author, email, date, msg = result.stdout.strip().split('|', 4)
                git_info['last_commit'] = {
                    'hash': hash[:7],
                    'author': author,
                    'date': date,
                    'message': msg
                }

            # Status
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=project_path,
                capture_output=True,
                text=True
            )
            git_info['has_changes'] = bool(result.stdout.strip())

        except Exception as e:
            git_info['error'] = str(e)

        return git_info

    def extract_summary(self, md_file):
        """Extract summary from markdown file"""
        try:
            content = md_file.read_text(encoding='utf-8')

            # Try to extract from frontmatter
            if content.startswith('---'):
                frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if frontmatter_match:
                    frontmatter = frontmatter_match.group(1)
                    # Look for description or summary field
                    desc_match = re.search(r'^(?:description|summary):\s*["\']?(.*?)["\']?$',
                                         frontmatter, re.MULTILINE | re.IGNORECASE)
                    if desc_match:
                        return desc_match.group(1).strip()

                    # Remove frontmatter for paragraph search
                    content = content[frontmatter_match.end():].strip()

            # Find first paragraph (non-heading, non-empty, no shortcodes)
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                # Skip empty, headings, code blocks, lists, HTML, and shortcodes
                if (line and
                    not line.startswith('#') and
                    not line.startswith('```') and
                    not line.startswith('-') and
                    not line.startswith('<') and
                    not line.startswith('{%') and
                    not line.startswith('{{%') and
                    not line.startswith('{{<') and
                    '{{% ' not in line and
                    '{{< ' not in line):
                    # Limit to 200 chars
                    if len(line) > 200:
                        return line[:197] + '...'
                    return line

            return "No summary available"

        except Exception as e:
            return f"Error reading file: {e}"

    def read_file_safe(self, file_path, max_chars=500):
        """Safely read file content"""
        try:
            content = file_path.read_text(encoding='utf-8')
            if len(content) > max_chars:
                return content[:max_chars] + '...'
            return content
        except:
            return "Could not read file"

    def save_inventory(self, output_file='inventory.json'):
        """Save inventory to JSON file"""
        inventory = self.scan_all()

        with open(output_file, 'w') as f:
            json.dump(inventory, f, indent=2)

        print(f"\n💾 Saved inventory to: {output_file}")
        return inventory

    def generate_project_profiles(self, projects_dir='projects'):
        """Generate markdown profile for each project"""
        os.makedirs(projects_dir, exist_ok=True)

        for project in self.projects:
            profile_path = os.path.join(projects_dir, f"{project['name']}.md")

            profile_content = f"""---
title: "{project['name']}"
date: {datetime.now().strftime('%Y-%m-%d')}
project_name: {project['name']}
is_git_repo: {project['is_git_repo']}
tech_stack: {', '.join(project['tech_stack']) if project['tech_stack'] else 'Unknown'}
---

# {project['name']}

## Overview

{project.get('readme_content', 'No description available')}

## Tech Stack

{', '.join(f'- {tech}' for tech in project['tech_stack']) if project['tech_stack'] else '- Unknown'}

## Files

**Total Markdown Files**: {len(project['markdown_files'])}

"""

            if project['markdown_files']:
                profile_content += "\n### Documentation\n\n"
                for md_file in project['markdown_files']:
                    profile_content += f"- [{md_file['name']}]({md_file['relative_path']})\n"
                    if md_file['summary']:
                        profile_content += f"  - {md_file['summary']}\n"

            if project['is_git_repo'] and 'git' in project:
                git = project['git']
                profile_content += "\n## Git Repository\n\n"
                if 'remote_url' in git:
                    profile_content += f"**URL**: [{git['remote_url']}]({git['remote_url']})\n\n"
                if 'branch' in git:
                    profile_content += f"**Branch**: {git['branch']}\n\n"
                if 'last_commit' in git:
                    lc = git['last_commit']
                    profile_content += f"**Last Commit**: {lc['message']} ({lc['date']}) by {lc['author']}\n\n"

            profile_content += f"\n**Path**: `{project['path']}`\n"
            if project['size_mb']:
                profile_content += f"**Size**: {project['size_mb']} MB\n"

            with open(profile_path, 'w') as f:
                f.write(profile_content)

            print(f"✅ Created profile: {profile_path}")


def main():
    scanner = ProjectScanner()

    # Scan all projects
    print("\n" + "="*60)
    print("PROJECT SCANNER")
    print("="*60 + "\n")

    inventory = scanner.save_inventory()

    # Generate project profiles
    print("\n📝 Generating project profiles...")
    scanner.generate_project_profiles()

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"\n✅ Projects scanned: {len(scanner.projects)}")
    print(f"📄 Markdown files found: {len(scanner.all_markdown_files)}")
    print(f"💾 Inventory saved: inventory.json")
    print(f"📁 Profiles created: projects/")
    print("\n" + "="*60 + "\n")


if __name__ == '__main__':
    main()
