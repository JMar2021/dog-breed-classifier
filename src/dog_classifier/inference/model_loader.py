import torch
from torchvision.models import resnet50, ResNet50_Weights
from dog_classifier.inference.model import LoadedModel

class ModelLoader:
    """Class responsible for loading the pre-trained ResNet50 model."""
    def load(self):
        """
        Load the pre-trained ResNet50 model.

        Returns:
            LoadedModel: An instance containing the loaded model and its weights.
        """
        weights = ResNet50_Weights.DEFAULT
        model = resnet50(weights=weights)
        model.eval()  #Inference mode
        return LoadedModel(model=model, weights=weights)