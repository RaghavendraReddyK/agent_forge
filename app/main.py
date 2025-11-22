from fastapi import FastAPI
from app.api.v1.routers import health,graph
import uvicorn

app = FastAPI(title="AgentForge")
app.include_router(health.router)
app.include_router(graph.router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug"
    )