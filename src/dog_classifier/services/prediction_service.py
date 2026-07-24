from pathlib import Path
import shutil
import tempfile

from fastapi import HTTPException, UploadFile
from dog_classifier.core.logger import get_logger
from dog_classifier.inference.predictor import InferenceService
from dog_classifier.schemas.api.prediction import PredictionResult

logger = get_logger(__name__)

class PredictionService:
    def __init__(self, inference_service: InferenceService):
        self.inference_service = inference_service

    def predict(self, file: UploadFile) -> PredictionResult:
        logger.info("Prediction request received: %s", file.filename)

        try:
            with tempfile.TemporaryDirectory() as tmp:
                image_path = Path(tmp) / file.filename

                with open(image_path, "wb") as tmp_file:
                    shutil.copyfileobj(file.file, tmp_file)

                result = self.inference_service.predict(str(image_path))

            logger.info(
                "Prediction completed: breed=%s confidence=%.2f",
                result.breed,
                result.confidence,
            )

            return result

        except Exception:
            logger.exception("Prediction failed")

            raise HTTPException(
                status_code=500,
                detail="Failed to process the uploaded file.",
            )