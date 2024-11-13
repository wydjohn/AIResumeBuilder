import os
from dotenv import load_dotenv
import requests
import json  # to handle payload formatting

load_dotenv()

class AIHelper:
    def __init__(self):
        self.api_key = os.getenv('AI_API_KEY')
        self.base_url = os.getenv('AI_API_BASE_URL')

    # Assume we can now pass a list of prompts
    def generate_text_batch(self, prompts, model="text-davinci-003"):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # Formulating payload for multiple prompts
        # This implementation assumes the API can handle a 'batch' of prompts. If not, this needs to be adjusted
        # to fit how the specific API can manage multiple requests efficiently (e.g., concurrent futures or async calls)
        payloads = [{
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 150,
            "top_p": 1.0,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "model": model
        } for prompt in prompts]
        
        # Example handling, may need to adjust based on API's actual batch support
        # Here we just iterate through payloads assuming only one is handled per call as a simplicity measure
        results = []
        for payload in payloads:
            response = requests.post(f"{self.base_url}/completions", json=payload, headers=headers)
            if response.status_code == 200:
                results.append(response.json()['choices'][0]['text'].strip())
            else:
                results.append("Error: Failed to generate text.")
        
        return results

if __name__ == "__main__":
    ai_helper = AIHelper()
    prompts = ["Explain the concept of machine learning in simple terms.",
               "Describe the difference between supervised and unsupervised learning."]
    generated_texts = ai_helper.generate_text_batch(prompts)
    
    for text in generated_texts:
        print(text)