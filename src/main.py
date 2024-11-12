from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict

app = FastAPI()

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "DevOps Demo App"}
    )

@app.get("/api/health")
def health_check() -> Dict[str, str]:
    return {"status": "healthy"}

@app.get("/api/stats")
def get_stats() -> Dict[str, int]:
    return {
        "deployments": 10,
        "uptime": 99.9,
        "users": 1234,
        "response_time": 250
    }