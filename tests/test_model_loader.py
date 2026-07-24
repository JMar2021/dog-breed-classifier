from dog_classifier.inference.model_loader import ModelLoader

def test_model_loader_loads_model():
    loaded_model = ModelLoader().load()
    assert loaded_model.model is not None
    assert loaded_model.weights is not None