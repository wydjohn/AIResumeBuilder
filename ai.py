import os
from dotenv import load_dotenv
import requests

load_dotenv()

class AIHelper:
    def __init__(self):
        self.api_key = os.getenv('AI_API_KEY')
        self.base_url = os.getenv('AI_API_BASE_URL')

    def generate_text(self, prompt, model="text-davinci-003"):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 150,
            "top_p": 1.0,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "model": model
        }
        
        response = requests.post(f"{self.base_url}/completions", json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()['choices'][0]['text'].strip()
        else:
            return "Error: Failed to generate text."

if __name__ == "__main__":
    ai_helper = AIHelper()
    prompt = "Explain the concept of machine learning in simple terms."
    generated_text = ai_helper.generate_text(prompt)
    print(generated_text)