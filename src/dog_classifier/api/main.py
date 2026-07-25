from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, Response
from prometheus_client import generate_latest
from dog_classifier.application import Application
from dog_classifier.core.logger import get_logger
from dog_classifier.schemas.api.prediction import PredictionResult
from dog_classifier.core.config import settings
from dog_classifier.core.state import state
from dog_classifier.core.exceptions import InferenceError, InvalidImageError

logger = get_logger(__name__)
app = FastAPI(title= settings.app_name, version = settings.version)
application = Application()

@app.exception_handler(InferenceError)
async def inference_error_handler(request, exc: InferenceError):
    logger.exception("Inference error occurred")
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )   

@app.exception_handler(InvalidImageError)
async def invalid_image_error_handler(request, exc: InvalidImageError):
    logger.exception("Invalid image error occurred")
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    logger.exception("An unexpected error occurred")
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred."}
    )
@app.get("/ready")
def readiness():
    logger.info("Readiness check requested")
    if state.model_loaded:
        return {"status": "ready"}
    else:
        return JSONResponse(
            status_code=503,
            content={"status": "not ready"}
        )
    
@app.get("/health")
def health():
    logger.info("Health check requested")
    return {
        "status": "alive"
    }

@app.get("/metrics")
def metrics():
    logger.info("Metrics requested")
    return Response(generate_latest(), media_type="text/plain; version=0.0.4; charset=utf-8")

@app.post("/predict", response_model=PredictionResult)
async def predict(file: UploadFile = File(...)):
    return application.prediction_service.predict(file)
    