from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Read the text from transcript.txt
with open(Path(__file__).parent / 'transcript.txt', 'r') as file:
    text = file.read()

# Call the OpenAI ChatGPT model
response = client.chat.completions.create(model='gpt-3.5-turbo',
messages=[{"role": "system", "content": "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."}, {"role": "user", "content": text}],
max_tokens=300,
temperature=0.7,
n=1,
stop=None)

# Get the generated answer
answer = response.choices[0].message

with open(Path(__file__).parent / "answer.txt", "w") as file:
    file.write(answer.content)