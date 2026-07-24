from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration.
    Values can come from environment variables.
    """

    app_name: str = "Dog Breed Classifier API"

    version: str = "0.1"

    log_level: str = "INFO"

    model_name: str = "resnet50"

    class Config:
        env_file = ".env"

settings = Settings()