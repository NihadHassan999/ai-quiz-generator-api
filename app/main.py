from fastapi import FastAPI
from app.routes import quiz_management, document_management, analytics
from app.database import engine, Base

app = FastAPI()

# Include routers
app.include_router(quiz_management.router, prefix="/api/quiz", tags=["Quiz Management"])
app.include_router(document_management.router, prefix="/api/files", tags=["Document Management"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
