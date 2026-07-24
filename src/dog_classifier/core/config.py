from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    app_name: str = "Dog Breed Classifier API"

    version: str = "0.1"

    log_level: str = "INFO"

    model_name: str = "resnet50"

    model_config = ConfigDict(
        env_file=".env"
    )


settings = Settings()