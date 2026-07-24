from dataclasses import dataclass
import torch

@dataclass
class LoadedModel:
    """Class to hold the loaded model and its weights."""
    model: torch.nn.Module
    weights: object