from dog_classifier.inference.model_loader import ModelLoader
from dog_classifier.inference.predictor import InferenceService
from dog_classifier.core.logger import configure_logging
from dog_classifier.services.prediction_service import PredictionService

class Application:
    "Main application class for the dog breed classifier."
    prediction_service: PredictionService
    def __init__(self):
        configure_logging()
        loaded_model = ModelLoader().load()
        self.inference_service = InferenceService(loaded_model)
        self.prediction_service = PredictionService(self.inference_service)