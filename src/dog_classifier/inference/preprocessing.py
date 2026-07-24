from PIL import Image, UnidentifiedImageError
from dog_classifier.core.exceptions import InvalidImageError

class ImagePreprocessor:
    """Preprocesses images for the dog breed classifier."""

    def __init__(self, weights):
        self.transform = weights.transforms()

    def process(self, image_path: str):
        """ Preprocess the image for inference."""
        # Load the image
        try:
            image = Image.open(image_path).convert("RGB")
        except UnidentifiedImageError as e :
            raise InvalidImageError("The uploaded file is not a valid image.") from e

        # Apply the preprocessing transform
        image = self.transform(image).unsqueeze(0)  # Add batch dimension
        
        return image