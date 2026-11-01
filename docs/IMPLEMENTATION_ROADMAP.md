# CMS and Visual Builder Roadmap

## Working rule

The current root-level static website stays available until the replacement is tested and ready. New platform work happens on the `cms-builder-foundation` branch. Do not merge unfinished infrastructure into the live branch.

## Phase 0: Architecture and safety baseline

- [x] Inspect the current static storefront and repository.
- [x] Create an isolated implementation branch.
- [x] Define the shared API, content model, page builder and publishing boundaries.
- [x] Record security requirements and non-goals.

## Phase 1: Backend foundation

- [ ] Create the FastAPI application and versioned API structure.
- [ ] Configure PostgreSQL connection and migrations.
- [ ] Add typed models for pages, sections, products, categories, media and settings.
- [ ] Add health and readiness endpoints.
- [ ] Add automated tests and API documentation.
- [ ] Add environment-based configuration and safe local development instructions.

## Phase 2: Authentication and media

- [ ] Add owner bootstrap flow and secure login/logout.
- [ ] Protect every admin endpoint.
- [ ] Add Cloudflare R2 storage adapter using server-side credentials.
- [ ] Add validated image upload, metadata, alt text and deletion safeguards.
- [ ] Test authorization and upload failure cases.

## Phase 3: Content management dashboard

- [ ] Build dashboard navigation and overview.
- [ ] Add product and category management.
- [ ] Add media library.
- [ ] Add page text, site settings and contact settings editors.
- [ ] Add draft save and validation.

## Phase 4: Visual page builder

- [ ] Define typed section schemas and defaults.
- [ ] Add section insertion, deletion, duplication and reordering.
- [ ] Add section-specific settings forms.
- [ ] Add desktop and mobile preview.
- [ ] Add page-level validation and draft preview.

## Phase 5: Publishing and storefront integration

- [ ] Add revision history and rollback.
- [ ] Add publish workflow.
- [ ] Connect the new storefront to published API content.
- [ ] Verify WhatsApp contact and navigation.
- [ ] Run accessibility, responsive, security and performance checks.
- [ ] Switch production only after owner approval and deployment verification.

## Phase 6: Future mobile app readiness

- [ ] Stabilize public API contracts.
- [ ] Document authentication and API versioning for mobile clients.
- [ ] Reuse product, category, page and site-setting APIs in the mobile app.

## Release gates

A phase is not complete because a screen looks finished. It must have working persistence, validation, authorization where required, tests, and a reproducible deployment path. Never claim image upload, publishing or authentication works until it has been tested end to end.
