# Backend API

This directory contains the FastAPI service shared by the public storefront, admin dashboard and future mobile app.

## Current implementation

- FastAPI application entry point
- Environment-based application settings
- Process and versioned API health endpoints
- Automated health endpoint tests

The database, authentication, content endpoints and object storage are not implemented yet.

## Local development

Use Python 3.11 or newer.

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
uvicorn app.main:app --reload
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Open `http://127.0.0.1:8000/docs` for the generated API documentation.

Run tests:

```bash
pytest
```

## Configuration

Settings are read from environment variables. A local `.env` file may be used for development, but it must never be committed. Do not put production secrets in source control.

## Architecture

PostgreSQL will be the source of truth for structured content. Image files will live in object storage, with metadata and object keys stored in PostgreSQL. Public endpoints will expose published content only; admin endpoints will require server-enforced authentication.

See [Platform Architecture](../docs/PLATFORM_ARCHITECTURE.md) and [Implementation Roadmap](../docs/IMPLEMENTATION_ROADMAP.md).
