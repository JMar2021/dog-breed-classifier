import torch
from torchvision.models import resnet50, ResNet50_Weights
from dog_classifier.inference.model import LoadedModel
from dog_classifier.core.logger import get_logger
from dog_classifier.core.metrics import model_info

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
        try:
            weights = ResNet50_Weights.DEFAULT
            model = resnet50(weights=weights)
            model.eval()  #Inference mode
            model_info.labels(model_name="resnet50",version="default",).set(1)
            logger.info("ResNet50 Model loaded successfully")
            return LoadedModel(model=model, weights=weights)
        except Exception as e:
            logger.error("Failed to load ResNet50 Model")
            raise e