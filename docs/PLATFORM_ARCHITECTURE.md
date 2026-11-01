# Platform Architecture

## Goal

Turn The Cozy Knot & Co. into a content-managed storefront with one owner dashboard. The dashboard must support both structured content editing and controlled visual page building. The public website and a future mobile app will consume the same backend API.

## Current state

The production-facing site is still the static HTML, CSS and JavaScript storefront at the repository root. It has no database, authenticated admin, API, media storage, or publishing workflow. Keep it working while the new platform is built separately.

## Proposed stack

- Public storefront: Next.js and TypeScript
- Admin dashboard: Next.js and TypeScript, protected server-side
- API: Python and FastAPI
- Database: PostgreSQL
- Image/object storage: Cloudflare R2 through a server-side storage adapter
- Hosting: Cloudflare Pages or Workers-compatible frontend deployment, plus a separately hosted API and PostgreSQL service
- Future mobile client: consumes the same API

Hosting and storage providers must be checked for current limits and costs before deployment. Do not assume the complete stack is free.

## Application boundaries

1. Storefront: public pages and customer enquiry journeys.
2. Admin: authenticated owner and staff interface.
3. API: validation, authorization, content publishing and media metadata.
4. Database: source of truth for products, pages, sections, assets and settings.
5. Object storage: original and optimized image files. The database stores metadata and object keys, not image bytes.

## Content management

The admin must manage:

- Products: name, slug, category, description, price when supplied, availability, featured status and images.
- Categories and occasions.
- Media assets: upload, alt text, dimensions, file type, file size and usage references.
- Pages: title, slug, SEO metadata, publication status and ordered sections.
- Site settings: logo, brand assets, WhatsApp number and social links.
- Draft and published content.

Prices, delivery promises, product details and business claims must only be published after the owner supplies verified information.

## Visual page builder

Use a controlled section-based builder, not arbitrary HTML or unrestricted code editing.

A page is represented by an ordered list of typed sections. Each section has a stable ID, a known type, validated settings and an explicit order. Initial section types:

- Hero
- Announcement strip
- Collection grid
- Occasion list
- Image and text story
- Featured products
- Promotional banner
- Contact / enquiry callout

The editor must support add, remove, reorder, duplicate, edit settings and preview. Desktop and mobile previews use the same content model. Each section type has a defined settings schema and responsive rendering rules.

Do not allow arbitrary script injection, raw HTML, or user-supplied CSS in the first version.

## Publishing model

- Editing changes a draft revision.
- Preview reads the draft revision.
- Publish validates the full page and promotes a revision to published.
- Public API reads published content only.
- Keep revision history so a previous published revision can be restored.
- A failed publish must not damage the current live page.

## Security requirements

- No public admin registration.
- Owner account creation must be an explicit deployment/setup step.
- Passwords are stored using a modern password hash, never plaintext.
- Use secure, HTTP-only cookies or an equivalent secure session mechanism.
- Enforce authorization on every admin API route.
- Validate upload MIME type, extension, size and image decoding. Generate random object keys.
- Never expose storage credentials or database credentials to browser code.
- Add rate limiting to authentication and upload endpoints.
- Keep secrets in deployment environment variables, never in Git.
- Log administrative changes without logging passwords, tokens or sensitive session data.

## API direction

Initial public endpoints:

- GET /api/v1/pages/{slug}
- GET /api/v1/products
- GET /api/v1/products/{slug}
- GET /api/v1/categories
- GET /api/v1/site-settings

Initial protected admin endpoints:

- POST /api/v1/admin/auth/login
- POST /api/v1/admin/auth/logout
- GET /api/v1/admin/me
- CRUD /api/v1/admin/products
- CRUD /api/v1/admin/categories
- CRUD /api/v1/admin/pages
- POST /api/v1/admin/media
- CRUD /api/v1/admin/site-settings
- POST /api/v1/admin/pages/{id}/publish
- GET /api/v1/admin/pages/{id}/revisions

All API contracts must be versioned and documented. The mobile app must use these same business APIs rather than duplicate business rules.

## Non-goals for the first CMS milestone

- Cart and checkout
- Online payment processing
- Inventory reservation
- Customer accounts
- Delivery partner integration
- Arbitrary drag-and-drop pixel positioning

These can be designed later without weakening the content platform.
