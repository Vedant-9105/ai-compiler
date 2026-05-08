from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import traceback

from backend.pipeline import run_pipeline

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Home route
@app.get("/")
async def home():
    return {
        "message": "AI Compiler Backend Running"
    }

# Frontend route
@app.get("/app")
async def serve_frontend():
    return FileResponse("frontend/index.html")

# Error handler
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
            "trace": traceback.format_exc()
        }
    )

# Generate endpoint
@app.post("/generate")
async def generate(request: Request):
    try:
        body = await request.json()
        prompt = body.get("prompt", "")

        result = run_pipeline(prompt)

        return result

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": str(e)
            }
        )