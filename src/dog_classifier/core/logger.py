import logging
from dog_classifier.core.config import settings

def configure_logging() -> None:
    level = getattr(logging, settings.log_level.upper())    
    logging.basicConfig(
        level=level,
        format=(
            "%(asctime)s "
            "%(levelname)s "
            "%(name)s "
            "%(message)s"
        ),
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)