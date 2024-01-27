from openai import OpenAI
import requests
client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
  prompt="a picture of munich in winter with a lot of children playing in the snow",
  size="1024x1024",
  quality="standard",
  n=1,
)
image_url = response.data[0].url
response = requests.get(image_url)
response.raise_for_status()

with open("winterMunich.jpg", "wb") as file:
    file.write(response.content)

print("Image file created successfully.")
