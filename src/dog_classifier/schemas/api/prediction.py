from pydantic import BaseModel

class PredictionResult(BaseModel):
    """Prediction result schema."""
    breed: str
    confidence: float