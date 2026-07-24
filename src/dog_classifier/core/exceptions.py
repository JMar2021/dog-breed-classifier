class DogClassifierError(Exception):
    """
    Base exception for application errors.
    """
    pass


class InvalidImageError(DogClassifierError):
    """
    Raised when the uploaded image cannot be processed.
    """
    pass


class InferenceError(DogClassifierError):
    """
    Raised when model inference fails.
    """
    pass