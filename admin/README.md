# Admin Dashboard

This directory is reserved for the authenticated owner dashboard and visual page builder.

The dashboard will manage structured business content and page layout through the shared FastAPI API. It must not keep production content only in browser storage or commit owner edits directly to the public Git repository.

Planned areas:

- Overview
- Products and categories
- Media library
- Pages and section builder
- Site settings
- Draft preview and publishing
- Revision history

The admin must be protected by server-enforced authentication. Hiding links in the interface is not access control.

See [Platform Architecture](../docs/PLATFORM_ARCHITECTURE.md) and [Implementation Roadmap](../docs/IMPLEMENTATION_ROADMAP.md).
