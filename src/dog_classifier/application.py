from dog_classifier.inference.model_loader import ModelLoader
from dog_classifier.inference.predictor import InferenceService
from dog_classifier.core.logger import configure_logging

class Application:
    "Main application class for the dog breed classifier."
    def __init__(self):
        configure_logging()
        loaded_model = ModelLoader().load()
        self.inference_service = InferenceService(loaded_model)