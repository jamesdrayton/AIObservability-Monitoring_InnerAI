from fastapi import APIRouter
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

router = APIRouter()

# --- Commands and helper function to add to metrics.py so that this module can receive the data ---
# from ..dashboard import metrics_dashboard as md
# md.processed_metrics(processed_json)

def processed_metrics(processed_json):
    print(processed_json)
    latency = processed_json.get("latency")

# md.record_latency("gpt-4", "user_prompt", latency=1.23)
# md.record_relevancy("gpt-4", "user_prompt", score=0.89)
# md.record_hallucination("gpt-4", "user_prompt")
# md.record_prompt("gpt-4", "user_prompt")


# --- Metrics Definitions ---

# TODO: Convert "model_name" to a global var received from metrics

# Histogram for latency tracking (seconds)
latency_histogram = Histogram(
    "llm_response_latency_seconds",
    "Latency of LLM responses in seconds",
    ["model_name"]
)

# Histogram for drift tracking (0-1)
drift_histogram = Histogram(
    "llm_drift_score",
    "Drift score of LLM responses (0 to 1)",
    ["model_name"]
)

# Gauge for relevancy score (0-1)
relevancy_score_gauge = Gauge(
    "llm_relevancy_score",
    "Relevancy score of LLM response (0 to 1)",
    ["model_name"]
)

# Counter for hallucination events
hallucination_counter = Counter(
    "llm_hallucination_total",
    "Total number of hallucinations detected in LLM responses",
    ["model_name"]
)

# Counter for total prompts received
prompt_counter = Counter(
    "llm_total_prompts",
    "Total number of prompts received by the middleware",
    ["model_name"]
)

# --- Metric Recording Functions ---

# Takes the model name and records the drift score to a histogram and updates a file
def record_drif(model_name: str, drift_score: float):
    drift_histogram.labels(model_name=model_name).observe(drift_score)

# Takes the model name and records it to 
def record_latency(model_name: str, latency: float):
    latency_histogram.labels(model_name=model_name).observe(latency)

def record_relevancy(model_name: str, score: float):
    relevancy_score_gauge.labels(model_name=model_name).set(score)

def record_hallucination(model_name: str):
    hallucination_counter.labels(model_name=model_name).inc()

def record_prompt(model_name: str):
    prompt_counter.labels(model_name=model_name).inc()

# --- Prometheus Metrics Endpoint ---

@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
