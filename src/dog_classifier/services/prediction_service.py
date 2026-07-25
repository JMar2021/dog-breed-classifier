from pathlib import Path
import shutil
import tempfile
import time
from fastapi import UploadFile
from dog_classifier.core.logger import get_logger
from dog_classifier.core.exceptions import InferenceError, DogClassifierError
from dog_classifier.inference.predictor import InferenceService
from dog_classifier.schemas.api.prediction import PredictionResult
from dog_classifier.core.metrics import (
    prediction_requests,
    prediction_failures,
    prediction_latency,
)

logger = get_logger(__name__)

class PredictionService:
    def __init__(self, inference_service: InferenceService):
        self.inference_service = inference_service

    def predict(self, file: UploadFile) -> PredictionResult:
        prediction_requests.inc()
        start_time = time.perf_counter()
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
            elapsed = time.perf_counter() - start_time
            prediction_latency.observe(elapsed)

            return result

        except DogClassifierError as e:
            prediction_failures.inc()
            raise e
        
        except Exception as e:
            prediction_failures.inc()
            logger.exception("Prediction failed")
            raise InferenceError("Failed to process the uploaded file.") from e