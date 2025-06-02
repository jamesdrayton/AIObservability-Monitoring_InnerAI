from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import os

# Set your API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCxAjRIrQnhytFkO2y5YXskO6Ck4zcYU0U"

# Initialize Gemini model
llm_base = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")
llm_v2 = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")

embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

latency_history = [50, 75, 60, 120]
token_usage_history = [500, 750, 600, 1200]

metric_template = """
    You are a specialist in tracking and evaluation the performance of results from prompts

    You will be given variables such as latency, given in milliseconds (ms) and token usage. Using this information, you must return whether there is an anomaly or not.

    You will also be given a history for previous latenciues and token usages. This will be used as your reference and comparison point.

    Additionally, you should use your own common knowledge to determine an answer and validate the response to not include any unnecessary information.

    Give the response as either "Normal" or "Anomaly" and provide reasoning behind the decision and how to improve sumarrized in 5 bullet points.

    latency: {latency}
    token_usage: {token_usage}

    latency_history: {latency_history}
    token_usage_history: {token_usage_history}
    """

# Create the chat prompt template
prompt = ChatPromptTemplate.from_template(metric_template)

# Create a chain with the model and the prompt
chain = prompt | llm_base

# Run the chain with a specific input

def evaluate_metrics(latency, token_usage, drift_threshold = 0.85):
    chain_base = prompt | llm_base
    chain_v2 = prompt | llm_v2

    response_base = chain_base.invoke({
        "latency": latency,
        "token_usage": token_usage,
        "latency_history": latency_history,
        "token_usage_history": token_usage_history}).content

    response_v2 = chain_v2.invoke({
        "latency": latency,
        "token_usage": token_usage,
        "latency_history": latency_history,
        "token_usage_history": token_usage_history}).content

        # Get responses
    # response_current = chain_current.invoke(input_data).content.strip()
    # response_baseline = chain_baseline.invoke(input_data).content.strip()

    # Embedding comparison for drift detection
    vec_base = embedding_model.embed_query(response_base)
    vec_v2 = embedding_model.embed_query(response_v2)
    similarity = cosine_similarity([vec_base], [vec_v2])[0][0]

    # Determine drift
    drift_status = "Drift Detected" if similarity < drift_threshold else "No Drift"

    print("\n--- Evaluation ---")
    print(f"Latency: {latency} ms | Token Usage: {token_usage} tokens")
    print(f"Response (Current):\n{response_base}")
    print(f"Response (Baseline):\n{response_v2}")
    print(f"Cosine Similarity: {similarity:.3f} --> {drift_status}")
    print("-------------------")

    token_usage_history.append(token_usage)
    latency_history.append(latency)

evaluate_metrics(100, 100)
evaluate_metrics(10, 1000)
evaluate_metrics(50, 600)