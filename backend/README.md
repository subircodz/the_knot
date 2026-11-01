# Backend API

This directory is reserved for the FastAPI service used by the public storefront, admin dashboard and future mobile app.

PostgreSQL will be the source of truth for structured content. Image files will live in object storage, with metadata and object keys stored in PostgreSQL.

The API must separate public published-content endpoints from authenticated admin endpoints. All configuration and credentials must come from environment variables.

See [Platform Architecture](../docs/PLATFORM_ARCHITECTURE.md) and [Implementation Roadmap](../docs/IMPLEMENTATION_ROADMAP.md).
