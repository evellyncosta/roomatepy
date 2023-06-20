from fastapi import FastAPI
from app.routes.room import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

