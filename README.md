# SAP SuccessFactors configuration demo

This repository contains a small portfolio example based on my previous work with SAP SuccessFactors Recruiting Management and employee data models.

The public files were rebuilt for the portfolio. Organization names, internal identifiers, tenant-specific rules, personal data fields and client-specific configuration were removed or replaced.

## What is included

- `xml/candidate-profile-template-demo.xml` - a neutral candidate profile template with standard and custom fields, picklists, permissions and display settings.
- `xml/succession-data-model-demo.xml` - a compact employee data model with multilingual labels, custom fields, background elements and permissions.
- `docs/field-catalog.csv` - a readable catalog of the fields used in both examples.
- `docs/anonymization-notes.md` - what was changed before publication.
- `scripts/validate_xml.py` - a small validation script that checks XML well-formedness and required root elements.

## What this demonstrates

- analysis of HR data structures;
- configuration of standard and custom fields;
- RU/EN localization;
- picklist references;
- role-based field access;
- background elements for repeating data;
- preparation of technical artifacts for review and version control.

## Important note

These files are portfolio examples. They are well-formed XML, but they are not intended for direct import into a production tenant without validation against the tenant version, DTD, permissions model and business rules.

## Validation

Run:

```bash
python scripts/validate_xml.py
```
