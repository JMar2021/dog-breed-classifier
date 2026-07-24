import typer
from pathlib import Path
from dog_classifier.inference.predictor import InferenceService
app = typer.Typer()

@app.command()
def version():
    print("Dog Breed Classifier v0.1")

@app.command()
def hello():
    """Test the CLI."""
    typer.echo("Hello from dog classifier!")

@app.command()
def predict(image_path: str):
    if not Path(image_path).exists():
        typer.echo(f"Error: The file '{image_path}' does not exist.")
        raise typer.Exit(code=1)
    service = InferenceService()
    result = service.predict(image_path)
    typer.echo(f"Predicted Breed: {result.breed}")
    typer.echo(f"Confidence: {result.confidence}")

if __name__ == "__main__":
    app()