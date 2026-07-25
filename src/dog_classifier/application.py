from dog_classifier.inference.model_loader import ModelLoader
from dog_classifier.inference.predictor import InferenceService
from dog_classifier.core.logger import configure_logging, get_logger
from dog_classifier.core.state import state
from dog_classifier.services.prediction_service import PredictionService


logger = get_logger(__name__)


class Application:
    """
    Main application class for the dog breed classifier.
    """

    prediction_service: PredictionService

    def __init__(self):

        configure_logging()

        try:
            logger.info("Starting application initialization now")
            loaded_model = ModelLoader().load()
            self.inference_service = InferenceService(loaded_model)
            self.prediction_service = PredictionService(self.inference_service)
            state.model_loaded = True
            logger.info(
                "Application initialized successfully"
            )

        except Exception as e:

            state.model_loaded = False
            logger.exception(
                "Application initialization failed"
            )

            raise e