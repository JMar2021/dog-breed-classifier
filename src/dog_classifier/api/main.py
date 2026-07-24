from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from dog_classifier.application import Application
from dog_classifier.core.logger import get_logger
from dog_classifier.schemas.api.prediction import PredictionResult
from dog_classifier.core.config import settings

logger = get_logger(__name__)
app = FastAPI(title= settings.app_name, version = settings.version)
application = Application()

@app.get("/health")
def health():
    logger.info("Health check requested")
    return {
        "status": "healthy"
    }

@app.post("/predict", response_model=PredictionResult)
async def predict(file: UploadFile = File(...)):
    return application.prediction_service.predict(file)
    