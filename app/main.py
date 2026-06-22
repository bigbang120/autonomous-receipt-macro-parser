from fastapi import FastAPI
from app.api.routes.receipt import router

app = FastAPI(
    title="Receipt Macro Parser",
    version="1.0.0"
)

app.include_router(
    router,
    prefix="/api/v1"
)
