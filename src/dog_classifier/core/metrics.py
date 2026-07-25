from prometheus_client import Counter, Histogram, Gauge

prediction_requests = Counter("prediction_requests_total", "Total number of prediction requests")
prediction_failures = Counter("prediction_failures_total", "Total number of failed prediction requests")
prediction_latency = Histogram("prediction_latency_seconds", "Latency of prediction requests in seconds")
model_info = Gauge("model_info", "Information about the loaded model", ["model_name", "version"])
prediction_breed_count = Counter("prediction_breed_count", "Count of predictions per breed", ["breed"])
inference_latency = Histogram("inference_latency_seconds", "Latency of inference in seconds")