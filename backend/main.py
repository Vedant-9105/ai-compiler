from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from .pipeline import run_pipeline
from .runtime import generate_app
import json

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body["prompt"]
    config = run_pipeline(prompt)
    return config

@app.get("/download")
async def download(prompt: str):
    config = run_pipeline(prompt)
    zip_bytes = generate_app(config)
    return Response(content=zip_bytes, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=app.zip"})

# Serve frontend UI from /frontend folder
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")