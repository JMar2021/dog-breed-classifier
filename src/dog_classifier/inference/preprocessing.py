from PIL import Image

class ImagePreprocessor:
    """Preprocesses images for the dog breed classifier."""

    def __init__(self, weights):
        self.transform = weights.transforms()

    def process(self, image_path: str):
        """ Preprocess the image for inference."""
        # Load the image
        image = Image.open(image_path).convert("RGB")
        
        # Apply the preprocessing transform
        image = self.transform(image).unsqueeze(0)  # Add batch dimension
        
        return image