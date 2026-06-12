from fastapi import FastAPI
from app.api.routes import router as fizzbuzz_router
from app.api.health import router as health_router

app = FastAPI(
    title="FizzBuzz API",
    version="1.0.0"
)

app.include_router(fizzbuzz_router)
app.include_router(health_router)