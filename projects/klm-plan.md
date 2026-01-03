---
title: "klm-plan"
date: 2026-01-03
project_name: klm-plan
is_git_repo: True
tech_stack: Hugo, AWS Lambda, AWS CloudFront, GitHub Actions
---

# klm-plan

## Overview

# KLM Business Plan

A Hugo-based wiki for organizing business planning, product development, and strategic initiatives for KLM Insurance.

## Quick Links

- **🔒 Secure Site (HTTPS + Password)**: https://d1jrr6wppi7k7d.cloudfront.net
  - Username: `klm`
  - Password: `KLM2026Plan!`
- **🔐 S3 Bucket**: PRIVATE - Only accessible via CloudFront (secured with OAC)
- **Documentation**: See [claude.md](./claude.md) for complete workflow guide
- **Security Setup**: See [SECURITY-SETUP.md](./SECURITY-SET...

## Tech Stack

- Hugo, - AWS Lambda, - AWS CloudFront, - GitHub Actions

## Files

**Total Markdown Files**: 72


### Documentation

- [planning.md](planning.md)
  - title: KLM Product Ideas
- [AUTOMATION-SUMMARY.md](AUTOMATION-SUMMARY.md)
  - A **complete automation system** for deploying secure Hugo documentation sites to AWS with a single command, based on the entire klm-plan setup process.
- [ACCESS-INFO.md](ACCESS-INFO.md)
  - **URL**: https://d1jrr6wppi7k7d.cloudfront.net
- [HUGO-AUTOMATION-SYSTEM.md](HUGO-AUTOMATION-SYSTEM.md)
  - We've created a **complete automation system** for deploying secure Hugo documentation sites to AWS with a single command. This system was built based on the klm-plan setup process and can be used ...
- [COMPLETE-SETUP-GUIDE.md](COMPLETE-SETUP-GUIDE.md)
  - This document captures the **complete process** we followed to create a secure, production-ready Hugo documentation site with AWS hosting, HTTPS, password protection, and automated deployment.
- [NAVIGATION-FIX.md](NAVIGATION-FIX.md)
  - After securing the S3 bucket (making it private with CloudFront OAC), navigation links stopped working and returned **403 AccessDenied** errors.
- [README.md](README.md)
  - A Hugo-based wiki for organizing business planning, product development, and strategic initiatives for KLM Insurance.
- [PERMISSIONS-SETUP.md](PERMISSIONS-SETUP.md)
  - All permissions have been configured to auto-approve for ALL future sessions across ALL projects in `/Users/mark/PycharmProjects` and its subdirectories.
- [S3-SECURITY-COMPLETE.md](S3-SECURITY-COMPLETE.md)
  - | Access Method | Status | Result |
- [SECURITY-SETUP.md](SECURITY-SETUP.md)
  - ✅ **CloudFront Distribution Created**
- [claude.md](claude.md)
  - This repository contains business planning documents, product ideas, and strategic planning for KLM Insurance. The content is organized using Hugo and published automatically to AWS S3 for easy acc...
- [default.md](archetypes/default.md)
  - +++
- [_index.md](content/_index.md)
  - Welcome to the KLM business planning workspace. This site organizes our strategic thinking, product development, and operational planning across all business lines.
- [README.md](themes/hugo-book/README.md)
  - [![Hugo](https://img.shields.io/badge/hugo-0.146-blue.svg)](https://gohugo.io)
- [docs.md](themes/hugo-book/archetypes/docs.md)
  - No summary available
- [posts.md](themes/hugo-book/archetypes/posts.md)
  - No summary available
- [_index.md](themes/hugo-book/exampleSite/content.zh/_index.md)
  - {{% columns %}}
- [showcases.md](themes/hugo-book/exampleSite/content.en/showcases.md)
  - <div class="book-hero text-center">
- [_index.md](themes/hugo-book/exampleSite/content.en/_index.md)
  - <div class="book-hero">
- [_index.md](themes/hugo-book/exampleSite/content.he/_index.md)
  - {{% columns %}}
- [creating-a-new-theme.md](themes/hugo-book/exampleSite/content.en/posts/creating-a-new-theme.md)
  - This tutorial will show you how to create a simple theme in Hugo. I assume that you are familiar with HTML, the bash command line, and that you are comfortable using Markdown to format content. I'l...
- [migrate-from-jekyll.md](themes/hugo-book/exampleSite/content.en/posts/migrate-from-jekyll.md)
  - Jekyll has a rule that any directory not starting with `_` will be copied as-is to the `_site` output. Hugo keeps all static content under `static`. You should therefore move it all there.
- [hugoisforlovers.md](themes/hugo-book/exampleSite/content.en/posts/hugoisforlovers.md)
  - +++
- [goisforlovers.md](themes/hugo-book/exampleSite/content.en/posts/goisforlovers.md)
  - +++
- [_index.md](themes/hugo-book/exampleSite/content.en/posts/_index.md)
  - No summary available
- [hidden.md](themes/hugo-book/exampleSite/content.en/docs/example/hidden.md)
  - Lorem markdownum arma ignoscas vocavit quoque ille texit mandata mentis ultimus,
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/example/_index.md)
  - Lorem markdownum, a quoque nutu est *quodcumque mandasset* veluti. Passim
- [buttons.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/buttons.md)
  - Buttons are styled links that can lead to local page or external link.
- [columns.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/columns.md)
  - Columns help organize shorter pieces of content horizontally for readability. `columns` shortcode styles markdown list as up to 3 columns.
- [details.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/details.md)
  - Details shortcode is a helper for `details` html5 element. To collapse the details either omit the `open`
- [hints.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/hints.md)
  - Hint shortcode can be used as a hint/alert/notification block.
- [tabs.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/tabs.md)
  - Tabs let you organize content by context, for example installation instructions for each supported platform.
- [steps.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/steps.md)
  - Steps shortcode styles numbered list as series of points for better content organization.
- [katex.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/katex.md)
  - KaTeX shortcode let you render math typesetting in markdown document. See [KaTeX](https://katex.org/)
- [mermaid.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/mermaid.md)
  - [MermaidJS](https://mermaid-js.github.io/) is library for generating svg charts and diagrams from text.
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/_index.md)
  - No summary available
- [images.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/images.md)
  - > [!WARNING]
- [badges.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/badges.md)
  - > [!WARNING]
- [asciinema.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/asciinema.md)
  - > [!WARNING]
- [cards.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/cards.md)
  - > [!WARNING]
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/_index.md)
  - No summary available
- [first-page.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/section/first-page.md)
  - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi u...
- [second-page.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/section/second-page.md)
  - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi u...
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/shortcodes/section/_index.md)
  - Section renders pages in section as definition list, using title and description. Optional param `summary` can be used to show or hide page summary
- [with-toc.md](themes/hugo-book/exampleSite/content.en/docs/example/table-of-contents/with-toc.md)
  - Lorem markdownum pavent auras, surgit nunc cingentibus libet **Laomedonque que**
- [without-toc.md](themes/hugo-book/exampleSite/content.en/docs/example/table-of-contents/without-toc.md)
  - Lorem markdownum pectora novis patenti igne sua opus aurae feras materiaque
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/example/table-of-contents/_index.md)
  - Lorem markdownum partu paterno Achillem. Habent amne generosi aderant ad pellem
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/example/collapsed/_index.md)
  - No summary available
- [4th-level.md](themes/hugo-book/exampleSite/content.en/docs/example/collapsed/3rd-level/4th-level.md)
  - Inde aderam facti; Theseus vis de tauri illa peream. Oculos **uberaque** non
- [_index.md](themes/hugo-book/exampleSite/content.en/docs/example/collapsed/3rd-level/_index.md)
  - Nefas discordemque domino montes numen tum humili nexilibusque exit, Iove. Quae
- [_index.md](content/lines-of-business/_index.md)
  - KLM operates across three main insurance verticals:
- [sales-process.md](content/sales-operations/sales-process.md)
  - Standardized sales process from lead to close and beyond.
- [comp.md](content/sales-operations/comp.md)
  - Compensation design that incentivizes new business, retention, cross-selling, and platform adoption.
- [_index.md](content/sales-operations/_index.md)
  - Sales processes, compensation structures, and operational procedures for KLM Insurance.
- [_index.md](content/products/_index.md)
  - Strategic product development for KLM, focusing on life and legacy planning services that complement our insurance offerings.
- [facebook.md](content/marketing/facebook.md)
  - Facebook advertising and organic presence for lead generation and brand building.
- [plan.md](content/marketing/plan.md)
  - KLM's marketing strategy focuses on differentiation through our life & legacy platform while maintaining competitive positioning in traditional insurance lines.
- [_index.md](content/marketing/_index.md)
  - Marketing plans and initiatives for KLM Insurance.
- [_index.md](content/products/new-ideas/_index.md)
  - A secure portal where clients and their families store key documents, instructions, and wishes alongside their policies. This can bundle multiple planning needs into one recurring product.[seasonsh...
- [document-collection.md](content/products/worst-case-scenario-planner/document-collection.md)
  - A structured system for identifying, organizing, and storing critical documents that families need during emergencies or transitions.
- [_index.md](content/products/worst-case-scenario-planner/_index.md)
  - Tools and resources to help families prepare for and navigate major life transitions, particularly end-of-life scenarios.
- [survivorship-playbook.md](content/products/worst-case-scenario-planner/survivorship-playbook.md)
  - **Status**: Phase 1 - Core Platform Module
- [_index.md](content/products/digital-life-vault/_index.md)
  - **Status**: Phase 1 - Core Platform Module
- [bop.md](content/lines-of-business/commercial-lines/bop.md)
  - Packaged commercial insurance for small to medium-sized businesses.
- [apartments.md](content/lines-of-business/commercial-lines/apartments.md)
  - Insurance for multi-family residential properties including apartments, duplexes, and larger complexes.
- [_index.md](content/lines-of-business/commercial-lines/_index.md)
  - Commercial insurance solutions for businesses.
- [_index.md](content/lines-of-business/life-insurance/_index.md)
  - Life insurance and our innovative life & legacy planning platform represent a strategic growth area for KLM.
- [boat.md](content/lines-of-business/personal-lines/boat.md)
  - Watercraft insurance for personal recreational vessels.
- [auto.md](content/lines-of-business/personal-lines/auto.md)
  - Auto insurance coverage for personal vehicles.
- [home.md](content/lines-of-business/personal-lines/home.md)
  - Homeowners insurance protecting property and liability.
- [liability.md](content/lines-of-business/personal-lines/liability.md)
  - Excess liability coverage that sits above auto and home policies.
- [_index.md](content/lines-of-business/personal-lines/_index.md)
  - Personal lines insurance protects individuals and families from financial loss.

## Git Repository

**URL**: [https://github.com/emmalone/klm-plan](https://github.com/emmalone/klm-plan)

**Branch**: main

**Last Commit**: Add Hugo documentation site automation system (5 minutes ago) by Mark Malone


**Path**: `/Users/mark/PycharmProjects/klm-plan`
**Size**: 20.85 MB
