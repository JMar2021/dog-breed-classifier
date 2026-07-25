# Dog Breed Classifier

ML-powered dog breed classification API built with FastAPI, Docker, and Kubernetes.

## Features

- Dog image classification API
- Dockerized application
- Kubernetes deployment
- Kubernetes Ingress routing
- Horizontal Pod Autoscaling
- Prometheus + Grafana monitoring
- Automated CI/CD with GitHub Actions

## Tech Stack

- Python / FastAPI
- PyTorch
- Docker
- Kubernetes
- GitHub Actions
- GHCR
- Prometheus
- Grafana


## Running Locally

Install dependencies:

```bash
uv sync

Run API:

uv run uvicorn dog_classifier.api.main:app --reload

Run tests:

uv run pytest
Kubernetes

Deploy:

kubectl apply -f k8s/

Application:

http://classifier.local

API Docs:

http://classifier.local/docs

Monitoring:

http://grafana.local
CI/CD

On push to main:

Run tests
Build Docker image
Push image to GHCR
Deploy to Kubernetes
Future
Helm charts
Kubernetes Secrets/ConfigMaps
GitOps with ArgoCD
Frontend upload interface