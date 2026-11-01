# The Cozy Knot & Co.

A responsive editorial-style storefront for a cake, gifting and celebration business.

## Current milestone: visual storefront

The current build is a static frontend using HTML, CSS and vanilla JavaScript.

- Editorial luxury and soft pastel visual direction
- Responsive desktop and mobile layouts
- Brand-led homepage and collection discovery
- Occasion-led browsing
- Brand story and enquiry section
- Accessible mobile navigation and reduced-motion support
- Basic search metadata

This is a visual storefront, not yet a transactional e-commerce platform. Collection links are enquiry placeholders. There is no live product catalogue, cart, checkout, payment processing, customer account, inventory or order management yet.

## Run locally

No build tools or package installation are required.

1. Clone the repository.
2. Open `index.html` in a browser.

For a local development server, use the Live Server extension in VS Code.

## Before launch

Replace temporary photography and add verified business information.

Business details still to confirm:

- Official logo and brand guidelines
- Business location and delivery coverage
- Phone number, WhatsApp ordering number and official email
- Official social links
- Product catalogue, descriptions, variants and prices
- Order lead times, delivery fees and payment methods
- Corporate gifting process

Do not publish placeholder contact information as a real business contact.

## Future platform direction

The website should eventually become the customer-facing storefront for a shared commerce backend. A future mobile app can use the same APIs and business data rather than duplicating order, product and customer logic.

A possible architecture to evaluate before implementation:

- Frontend: Next.js and TypeScript
- API/backend: Python and FastAPI
- Database: PostgreSQL
- Payments: an India-supported payment gateway such as Razorpay, subject to account and business verification
- Future mobile app: React Native or another API-connected framework

These are proposed choices, not implemented dependencies.

## Project structure

```
the_knot/
├── index.html
├── styles.css
├── script.js
└── README.md
```
