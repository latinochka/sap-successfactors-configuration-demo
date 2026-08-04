# Anonymization notes

The source set contained several candidate profile variants and one employee data model. The public package consolidates them into two shorter examples.

Before publication, the following information was removed or changed:

- organization and project names;
- internal abbreviations and client-specific field IDs;
- tenant-specific picklists and workflow logic;
- fields that described unique programs, business units or security checks;
- unnecessary identity document and health-related fields;
- internal comments, file names and environment-specific references;
- broad permission blocks copied from a real tenant.

The demo keeps only the patterns needed to show the technical approach: field types, localization, picklist links, repeating blocks, permissions and display configuration.

No original source file should be committed to the public repository.
