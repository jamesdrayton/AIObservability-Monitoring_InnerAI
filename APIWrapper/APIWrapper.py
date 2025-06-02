# Gemini Wrapper 

import time
import logging
import google.generativeai as genai

# Configure logging
logging.basicConfig(
    filename="gemini_calls.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

class GeminiMiddleware:
    def __init__(self, api_key: str, model_name: str = "gemini-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str, max_tokens: int = 256, temperature: float = 0.7, metadata: dict = None):
        if metadata is None:
            metadata = {}

        log_entry = {
            "prompt": prompt,
            "metadata": metadata,
            "model": self.model._model_name,
        }

        try:
            start_time = time.time()
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": max_tokens,
                    "temperature": temperature,
                }
            )
            duration = time.time() - start_time

            log_entry.update({
                "response": response.text.strip(),
                "latency_sec": round(duration, 3),
                "status": "success"
            })

            logging.info(log_entry)
            return response.text.strip()

        except Exception as e:
            duration = time.time() - start_time
            log_entry.update({
                "error": str(e),
                "latency_sec": round(duration, 3),
                "status": "error"
            })

            logging.error(log_entry)
            return None