from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Read the text from transcript.txt
with open(Path(__file__).parent / 'transcript.txt', 'r') as file:
    text = file.read()

# Call the OpenAI ChatGPT model
response = client.chat.completions.create(model='gpt-3.5-turbo',
messages=[{"role": "system", "content": "The following text is a question or a prompt of a laywer. The assistant helps the laywer in doing his work with advises. The answer should not be longer than 3 sentences. The text in the claim is:\
           "}, {"role": "user", "content": text}],
max_tokens=300,
temperature=0.7,
n=1,
stop=None)

# Get the generated answer
answer = response.choices[0].message
speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="shimmer",
  input=answer.content) as response:
  response.stream_to_file(speech_file_path)