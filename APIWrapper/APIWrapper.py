# Gemini Wrapper 

import google.generativeai as genai

class GeminiWrapper:
    def __init__(self, api_key, model_name='gemini-2.0-flash'):
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt, max_tokens=256, temperature=0.7):
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "max_output_tokens": max_tokens,
                    "temperature": temperature,
                }
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"