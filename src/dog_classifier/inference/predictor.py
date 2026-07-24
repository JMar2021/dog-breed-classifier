import torch
from dog_classifier.schemas.api.prediction import PredictionResult
from dog_classifier.inference.preprocessing import ImagePreprocessor
from dog_classifier.inference.model import LoadedModel
from dog_classifier.core.logger import get_logger

logger = get_logger(__name__)

class InferenceService:
    """Service for performing inference on dog breed images."""
    def __init__(self, loaded_model: LoadedModel):
        self.model = loaded_model.model
        self.weights = loaded_model.weights
        self.preprocessor = ImagePreprocessor(self.weights)
        self.categories = self.weights.meta["categories"]

    def predict(self, image_path: str) -> PredictionResult:
        """
        Predict the dog breed from the given image.

        Args:
            image_path (str): Path to the image file.

        Returns:
            PredictionResult: The prediction result.
        """
        image = self.preprocessor.process(image_path)
        with torch.no_grad():
            output = self.model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        confidence, index = torch.max(probabilities, dim=0)
        breed = self.categories[index]
        logger.info("Prediction complete: breed=%s confidence=%.2f", breed, confidence) 
        return PredictionResult(breed=breed, confidence=float(confidence))