from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import traceback

app = FastAPI()

# Custom exception handler to always return JSON
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": str(exc), "trace": traceback.format_exc()}
    )

@app.post("/generate")
async def generate(request: Request):
    try:
        body = await request.json()
        prompt = body.get("prompt", "")
        # ... your pipeline call ...
        config = run_pipeline(prompt)  # replace with your actual function
        return config
    except Exception as e:
        # Return JSON error instead of raising
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )
        