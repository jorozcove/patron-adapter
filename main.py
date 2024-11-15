from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

def create_app():
    app = FastAPI()

    from src.supa.client import sb
    from src.middlewares.auth import CustomAuthMiddleware

    # Import and register the API endpoints
    from src.routes.users import users_router

    # Add middleware
    app.add_middleware(CustomAuthMiddleware, supabase=sb)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add the routers
    app.include_router(users_router, prefix="/users", tags=["users"])

    # Health check
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)