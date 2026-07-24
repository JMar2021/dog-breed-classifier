from dog_classifier.inference.model_loader import ModelLoader
from dog_classifier.inference.predictor import InferenceService

class Application:
    "Main application class for the dog breed classifier."
    def __init__(self):
        loaded_model = ModelLoader().load()
        self.inference_service = InferenceService(loaded_model)