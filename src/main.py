from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/")
def read_root() -> Dict[str, str]:
    return {"message": "Hello DevOps World!"}

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "healthy"}