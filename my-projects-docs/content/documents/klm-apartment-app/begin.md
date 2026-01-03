---
title: "begin"
project: klm-apartment-app
original_path: begin.md
modified: 2026-01-02T17:56:37.628095
---

This project is going to be focused on creating a new application called klm-appartment-app also known as KAA.  This will need a new github repo and new AWS resources, both github CLI and AWS CLI should be installed and configured.  

please create a new claude.md file for this project by include all of the information needed from ..\klm-migrate\claude.md

I have included a number of documented in this

The very first thing that needs to be done is get everything configured so that I can work with the same workflow as the ..\klm-migrate project.  I want to be able to develop locally as well as remotely with my iphone and deploy to new AWS buckets for dev, staging and production when this is finally completed.

I want the next task to be using the \model opus to review all of the documents and instructions and requirements in the project and all subfolders and to think deeply about the problem domain and the best way to approach the solutions.

Then I want to switch to development with claude code having all of the required files, data, permissions to write code deploy it locally, write test cases, execute the test cases, identify bugs and fix them, retest.

The current MVP that I want to demostrate my test on is focues on building a local python application that will analysis all of the data available for Eugene Mark Malone (me) and my 2 investment properties on Prince street and Middle Spring.  This MVP should use SQLite as the database to create the data model that will organize the insured, the properties, the carriers and all of the data.

The immediate target is to be able to collect all of the data about me, identify what data is missing from the required forms which are ACORD 125 and 140 and the Miller Supplemental application.  The Miller Supplemental app is currently partially filled out.  Use this to collect data for the database.  There is a clean version of this form to use as a template.  The ACORD forms are clean and fillable.

The success of the MVP includes

1. the collection of the existing data from the files on hand.  This can be submitted to claude via API using Sonnet as a model if needed.
2. the creation and persistance of the database structure and all of the data for the insured, properties, data, carriers and applications ready to submit
3. identification of missing data and a structured request for the insured to provide a reply
4. the completion of ACORD forms 125 and 140 with all of the needed infomation for a quote.  Use claude api as needed, for a single application for Eugene Mark Malone
4. the completion of the Miller Supplemental app, for a single application for Eugene Mark Malone

If possible while building the MVP and dev version of this app please use my personal Max plan for Claude access.  When it goes into production I will want to shift to using an API key to pay per use

Please confirm, ask any questions needed to get started then proceed.

