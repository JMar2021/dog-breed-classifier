from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from dog_classifier.application import Application
from dog_classifier.core.logger import get_logger
import shutil
import tempfile

logger = get_logger(__name__)
app = FastAPI(title= "Dog Breed Classifier API", version = "0.1")
application = Application()

@app.get("/health")
def health():
    logger.info("Health check requested")
    return {
        "status": "healthy"
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    logger.info("Prediction request received")
    with tempfile.TemporaryDirectory() as tmp:
        image_path = Path(tmp) / file.filename
        with open(image_path, "wb") as tmp_file:
            shutil.copyfileobj(file.file, tmp_file)
        try:
            result = application.inference_service.predict(image_path)
        except Exception as e:
            logger.exception("Error occurred while making prediction: %s", str(e))
            raise
    logger.info("Prediction completed: breed=%s confidence=%.2f", result.breed, result.confidence)
    return {
        "breed": result.breed,
        "confidence": result.confidence
    }

