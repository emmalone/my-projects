#!/usr/bin/env python3
"""
Documentation Generator - Create Hugo site from all project markdown files

Reads inventory.json and generates a Hugo documentation site that includes:
- All markdown files from all projects
- Project overviews
- Document index organized by project
- Cross-project search

Usage:
    python3 generate-docs.py
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime
import re

class DocumentationGenerator:
    def __init__(self, inventory_file='inventory.json', output_dir='my-projects-docs'):
        self.inventory_file = inventory_file
        self.output_dir = output_dir
        self.content_dir = os.path.join(output_dir, 'content')
        self.inventory = None

    def load_inventory(self):
        """Load project inventory"""
        with open(self.inventory_file, 'r') as f:
            self.inventory = json.load(f)
        print(f"✅ Loaded inventory: {len(self.inventory['projects'])} projects")

    def create_hugo_site(self):
        """Create Hugo site structure"""
        print(f"🏗️  Creating Hugo site: {self.output_dir}")

        # Create Hugo site if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Create content directories
        os.makedirs(f"{self.content_dir}/projects", exist_ok=True)
        os.makedirs(f"{self.content_dir}/documents", exist_ok=True)
        os.makedirs(f"{self.content_dir}/inventory", exist_ok=True)

        print("✅ Hugo site structure created")

    def create_hugo_config(self):
        """Create hugo.toml configuration"""
        config = f'''baseURL = 'http://localhost:1313/'
languageCode = 'en-us'
title = 'My Projects - Documentation Hub'
theme = 'hugo-book'

[params]
  BookRepo = 'https://github.com/emmalone/my-projects'
  BookSearch = true
  BookToC = true
  BookComments = false
  BookMenuBundle = '/menu'

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.tableOfContents]
    startLevel = 1
    endLevel = 3
'''

        with open(f"{self.output_dir}/hugo.toml", 'w') as f:
            f.write(config)

        print("✅ Hugo config created")

    def create_homepage(self):
        """Create homepage with project overview"""
        homepage = f'''---
title: "My Projects"
type: docs
---

# My Projects Documentation Hub

Welcome to the central documentation hub for all projects in PycharmProjects.

**Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Quick Stats

- **Total Projects**: {len(self.inventory['projects'])}
- **Total Documents**: {len(self.inventory['markdown_files'])}
- **Last Scan**: {self.inventory['scan_date']}

## Navigation

- [Projects Overview]({{{{< relref "/projects" >}}}}) - All projects with status and tech stack
- [Documents Index]({{{{< relref "/documents" >}}}}) - All markdown files organized by project
- [Inventory]({{{{< relref "/inventory" >}}}}) - Detailed project inventory

## Recent Projects

'''

        # Add recent projects (sort by last modified)
        projects_with_git = [p for p in self.inventory['projects'] if 'git' in p and 'last_commit' in p.get('git', {})]
        if projects_with_git:
            # Sort by commit date
            for project in projects_with_git[:5]:
                git = project['git']
                lc = git.get('last_commit', {})
                homepage += f"- **[{project['name']}]({{{{< relref \"/projects/{project['name']}\" >}}}})** - {lc.get('message', 'No commit message')} ({lc.get('date', 'Unknown')})\n"

        homepage += "\n## Tech Stack Used\n\n"

        # Collect all tech stack items
        all_tech = set()
        for project in self.inventory['projects']:
            all_tech.update(project.get('tech_stack', []))

        for tech in sorted(all_tech):
            projects_with_tech = [p['name'] for p in self.inventory['projects'] if tech in p.get('tech_stack', [])]
            homepage += f"- **{tech}** ({len(projects_with_tech)} projects)\n"

        with open(f"{self.content_dir}/_index.md", 'w') as f:
            f.write(homepage)

        print("✅ Homepage created")

    def create_projects_index(self):
        """Create projects index page"""
        index = f'''---
title: "Projects"
type: docs
bookCollapseSection: false
---

# All Projects

{len(self.inventory['projects'])} projects found in PycharmProjects.

'''

        for project in self.inventory['projects']:
            tech_stack = ', '.join(project.get('tech_stack', [])) or 'Unknown'
            git_status = "📦 Git Repo" if project['is_git_repo'] else "📁 Directory"

            index += f"## [{project['name']}]({{{{< relref \"{project['name']}\" >}}}})\n\n"
            index += f"{git_status} | {tech_stack}\n\n"

            # Get first line of README if available
            if 'readme_content' in project:
                first_line = project['readme_content'].split('\n')[0]
                if first_line.startswith('#'):
                    first_line = first_line.lstrip('#').strip()
                index += f"{first_line}\n\n"

            index += f"**Documents**: {len(project.get('markdown_files', []))}\n\n"

            if project['is_git_repo'] and 'git' in project:
                git = project['git']
                if 'remote_url' in git:
                    index += f"[View on GitHub]({git['remote_url']})\n\n"

            index += "---\n\n"

        with open(f"{self.content_dir}/projects/_index.md", 'w') as f:
            f.write(index)

        print("✅ Projects index created")

    def create_project_pages(self):
        """Create individual project pages"""
        for project in self.inventory['projects']:
            project_file = f"{self.content_dir}/projects/{project['name']}.md"

            content = f'''---
title: "{project['name']}"
weight: 1
---

# {project['name']}

'''

            # Project info
            if project['is_git_repo']:
                content += "**Type**: Git Repository\n\n"
                if 'git' in project and 'remote_url' in project['git']:
                    content += f"**GitHub**: [{project['git']['remote_url']}]({project['git']['remote_url']})\n\n"
            else:
                content += "**Type**: Directory\n\n"

            # Tech stack
            if project.get('tech_stack'):
                content += "## Tech Stack\n\n"
                for tech in project['tech_stack']:
                    content += f"- {tech}\n"
                content += "\n"

            # README content
            if 'readme_content' in project:
                content += "## Overview\n\n"
                content += f"{project['readme_content']}\n\n"

            # Documentation files
            if project.get('markdown_files'):
                content += f"## Documentation ({len(project['markdown_files'])} files)\n\n"
                for md_file in project['markdown_files']:
                    # Create link to document in documents section
                    doc_link = f"/documents/{project['name']}/{md_file['name'].replace('.md', '')}"
                    content += f"### [{md_file['name']}]({{{{< relref \"{doc_link}\" >}}}})\n\n"
                    if md_file.get('summary'):
                        content += f"{md_file['summary']}\n\n"

            # Git info
            if project['is_git_repo'] and 'git' in project:
                git = project['git']
                content += "## Git Information\n\n"
                if 'branch' in git:
                    content += f"**Branch**: {git['branch']}\n\n"
                if 'last_commit' in git:
                    lc = git['last_commit']
                    content += f"**Last Commit**: {lc.get('message', 'N/A')}\n\n"
                    content += f"**Author**: {lc.get('author', 'N/A')} ({lc.get('date', 'N/A')})\n\n"
                if git.get('has_changes'):
                    content += "⚠️ **Status**: Uncommitted changes\n\n"

            content += f"\n**Path**: `{project['path']}`\n"

            with open(project_file, 'w') as f:
                f.write(content)

        print(f"✅ Created {len(self.inventory['projects'])} project pages")

    def create_documents_index(self):
        """Create documents index organized by project"""
        index = f'''---
title: "Documents"
type: docs
bookCollapseSection: false
---

# All Documents

{len(self.inventory['markdown_files'])} markdown files across all projects.

'''

        # Group by project
        docs_by_project = {}
        for md_file in self.inventory['markdown_files']:
            project = md_file['project']
            if project not in docs_by_project:
                docs_by_project[project] = []
            docs_by_project[project].append(md_file)

        for project_name in sorted(docs_by_project.keys()):
            docs = docs_by_project[project_name]
            index += f"## {project_name} ({len(docs)} documents)\n\n"

            for md_file in docs:
                doc_link = f"/documents/{project_name}/{md_file['name'].replace('.md', '')}"
                index += f"- [{md_file['name']}]({{{{< relref \"{doc_link}\" >}}}}) - {md_file.get('summary', 'No summary')}\n"

            index += "\n"

        with open(f"{self.content_dir}/documents/_index.md", 'w') as f:
            f.write(index)

        print("✅ Documents index created")

    def copy_document_files(self):
        """Copy all markdown files to Hugo content"""
        for md_file in self.inventory['markdown_files']:
            project_name = md_file['project']
            source_path = md_file['file_path']

            # Create project subdirectory
            project_docs_dir = f"{self.content_dir}/documents/{project_name}"
            os.makedirs(project_docs_dir, exist_ok=True)

            # Destination path
            dest_name = md_file['name']
            dest_path = os.path.join(project_docs_dir, dest_name)

            # Copy file
            try:
                shutil.copy2(source_path, dest_path)

                # Add frontmatter if not present
                self.add_frontmatter(dest_path, md_file)

            except Exception as e:
                print(f"⚠️  Error copying {md_file['name']}: {e}")

        print(f"✅ Copied {len(self.inventory['markdown_files'])} document files")

    def add_frontmatter(self, file_path, md_info):
        """Add or update frontmatter in markdown file"""
        try:
            content = Path(file_path).read_text(encoding='utf-8')

            # Check if frontmatter already exists
            if not content.startswith('---'):
                # Add frontmatter
                frontmatter = f'''---
title: "{md_info['name'].replace('.md', '')}"
project: {md_info['project']}
original_path: {md_info['relative_path']}
modified: {md_info['modified']}
---

'''
                content = frontmatter + content

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

        except Exception as e:
            print(f"⚠️  Error adding frontmatter to {file_path}: {e}")

    def create_inventory_page(self):
        """Create detailed inventory page"""
        content = f'''---
title: "Inventory"
type: docs
---

# Project Inventory

Complete inventory of all projects in PycharmProjects.

**Scan Date**: {self.inventory['scan_date']}

## Summary

- **Total Projects**: {len(self.inventory['projects'])}
- **Git Repositories**: {sum(1 for p in self.inventory['projects'] if p['is_git_repo'])}
- **Total Markdown Files**: {len(self.inventory['markdown_files'])}
- **Combined Size**: {sum(p.get('size_mb', 0) for p in self.inventory['projects']):.2f} MB

## Projects by Tech Stack

'''

        # Group by tech
        tech_projects = {}
        for project in self.inventory['projects']:
            for tech in project.get('tech_stack', ['Unknown']):
                if tech not in tech_projects:
                    tech_projects[tech] = []
                tech_projects[tech].append(project['name'])

        for tech in sorted(tech_projects.keys()):
            projects = tech_projects[tech]
            content += f"### {tech} ({len(projects)} projects)\n\n"
            for proj_name in sorted(projects):
                content += f"- [{proj_name}]({{{{< relref \"/projects/{proj_name}\" >}}}})\n"
            content += "\n"

        content += "## All Projects (Detailed)\n\n"

        for project in self.inventory['projects']:
            content += f"### {project['name']}\n\n"
            content += f"- **Path**: `{project['path']}`\n"
            content += f"- **Type**: {'Git Repository' if project['is_git_repo'] else 'Directory'}\n"
            if project.get('tech_stack'):
                content += f"- **Tech**: {', '.join(project['tech_stack'])}\n"
            if project.get('size_mb'):
                content += f"- **Size**: {project['size_mb']} MB\n"
            content += f"- **Documents**: {len(project.get('markdown_files', []))}\n"
            content += "\n"

        with open(f"{self.content_dir}/inventory/_index.md", 'w') as f:
            f.write(content)

        print("✅ Inventory page created")

    def install_theme(self):
        """Install hugo-book theme"""
        themes_dir = f"{self.output_dir}/themes"
        theme_path = f"{themes_dir}/hugo-book"

        if not os.path.exists(theme_path):
            print("📦 Installing hugo-book theme...")
            os.makedirs(themes_dir, exist_ok=True)

            # Use git submodule
            os.chdir(self.output_dir)
            try:
                subprocess.run(['git', 'init'], check=True, capture_output=True)
                subprocess.run([
                    'git', 'submodule', 'add',
                    'https://github.com/alex-shpak/hugo-book',
                    'themes/hugo-book'
                ], check=True)
                print("✅ Theme installed")
            except Exception as e:
                print(f"⚠️  Could not install theme as submodule: {e}")
            finally:
                os.chdir('..')
        else:
            print("✅ Theme already installed")

    def generate_all(self):
        """Generate complete documentation site"""
        print("\n" + "="*60)
        print("DOCUMENTATION GENERATOR")
        print("="*60 + "\n")

        self.load_inventory()
        self.create_hugo_site()
        self.create_hugo_config()
        self.install_theme()
        self.create_homepage()
        self.create_projects_index()
        self.create_project_pages()
        self.create_documents_index()
        self.copy_document_files()
        self.create_inventory_page()

        print("\n" + "="*60)
        print("COMPLETE!")
        print("="*60)
        print(f"\n✅ Hugo site generated: {self.output_dir}")
        print(f"📄 Projects: {len(self.inventory['projects'])}")
        print(f"📝 Documents: {len(self.inventory['markdown_files'])}")
        print("\n💡 Next steps:")
        print(f"   cd {self.output_dir}")
        print("   hugo server -D")
        print("   # Visit http://localhost:1313")
        print("\n" + "="*60 + "\n")


def main():
    import subprocess  # Import here for the install_theme method

    generator = DocumentationGenerator()
    generator.generate_all()


if __name__ == '__main__':
    import subprocess
    main()
