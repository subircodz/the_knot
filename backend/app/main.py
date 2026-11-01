from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Shared content API for the storefront, admin dashboard and future mobile app.",
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return process health without exposing secrets or infrastructure details."""
    return {"status": "ok"}


@app.get(f"{settings.api_v1_prefix}/health", tags=["health"])
def api_health_check() -> dict[str, str]:
    """Return versioned API health."""
    return {"status": "ok", "api": "v1"}
