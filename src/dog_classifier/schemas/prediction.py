from dataclasses import dataclass

@dataclass
class PredictionResult:
    """Prediction result schema."""
    breed: str
    confidence: float