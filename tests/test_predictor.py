from dog_classifier.inference.predictor import InferenceService

def test_predict_returns_prediction_result():
    service = InferenceService()
    result = service.predict("dummy_image_path.jpg")
    assert result.breed == "Golden Retriever"
    assert result.confidence == 0.95
