from fastapi import FastAPI
from src.json.controller import router as json_router

app = FastAPI()

app.include_router(json_router)