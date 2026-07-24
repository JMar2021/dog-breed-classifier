from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from dog_classifier.application import Application
from dog_classifier.core.logger import get_logger
from dog_classifier.schemas.api.prediction import PredictionResult
from dog_classifier.core.config import settings
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

@app.get("/health")
def health():
    logger.info("Health check requested")
    return {
        "status": "healthy"
    }

@app.post("/predict", response_model=PredictionResult)
async def predict(file: UploadFile = File(...)):
    return application.prediction_service.predict(file)
    