from openai import OpenAI
from app.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024"
    )
    return response.data[0].url

def generate_img(self, model: str, prompt: str, size: any, response_format: any):
    generation_response = client.images.generate(
        model=model,
        prompt=prompt,
        n=1,
        size=size,
        response_format=response_format,
        style="vivid"
    )
    return generation_response.data[0].url
