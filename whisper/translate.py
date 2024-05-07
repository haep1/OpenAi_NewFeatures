from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Read the text from transcript.txt
with open(Path(__file__).parent / 'transcript.txt', 'r') as file:
    text = file.read()

# Call the OpenAI ChatGPT model
#"The following text is a question or a prompt of a laywer. The assistant helps the laywer in doing his work with advises. The answer should not be longer than 3 sentences. The text belonging to the question is:
response = client.chat.completions.create(model='gpt-3.5-turbo',
messages=[{"role": "system", "content": "Translate this text to english:\
           "}, {"role": "user", "content": text}],
max_tokens=3000,
temperature=0.7,
n=1,
stop=None)

# Get the generated answer
answer = response.choices[0].message

# Save the answer to a file
with open(Path(__file__).parent / "english.txt", "w") as file:
    file.write(answer.content)
