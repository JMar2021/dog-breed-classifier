import torch
from torchvision.models import resnet50, ResNet50_Weights
from dog_classifier.inference.model import LoadedModel
from dog_classifier.core.logger import get_logger

logger = get_logger(__name__)

class ModelLoader:
    """Class responsible for loading the pre-trained ResNet50 model."""
    def load(self):
        """
        Load the pre-trained ResNet50 model.

        Returns:
            LoadedModel: An instance containing the loaded model and its weights.
        """
        logger.info("Loading ResNet50 Model")
        weights = ResNet50_Weights.DEFAULT
        model = resnet50(weights=weights)
        model.eval()  #Inference mode
        logger.info("ResNet50 Model loaded successfully")
        return LoadedModel(model=model, weights=weights)