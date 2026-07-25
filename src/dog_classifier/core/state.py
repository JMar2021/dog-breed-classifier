from dataclasses import dataclass


@dataclass
class ApplicationState:
    """
    Tracks application readiness.
    """

    model_loaded: bool = False


state = ApplicationState()