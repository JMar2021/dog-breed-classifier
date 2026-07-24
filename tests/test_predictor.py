from pathlib import Path

from PIL import Image

from dog_classifier.application import Application


def test_predict_returns_prediction(tmp_path: Path):

    image_path = tmp_path / "test.jpg"

    image = Image.new(
        "RGB",
        (224, 224),
        color="red",
    )

    image.save(image_path)

    application = Application()

    result = (
        application
        .inference_service
        .predict(str(image_path))
    )

    assert result.breed
    assert 0 <= result.confidence <= 1