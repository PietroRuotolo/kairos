from fastapi import FastAPI
from datetime import UTC, datetime

app = FastAPI()

@app.get("/")
async def home() -> dict[str, str | int]:
    return {
        "message": "Hello, world!",
        "now": datetime.now(tz=UTC).isoformat(),
        "counter": 1,
    }

@app.get("/health")
async def liveness() -> dict[str,str]:
    return{"status": "alive"}