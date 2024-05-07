from pathlib import Path
from openai import OpenAI

client = OpenAI()

# Read the text from transcript.txt
with open(Path(__file__).parent / 'translate.txt', 'r') as file:
    text = file.read()

speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
  model="tts-1-hd",
  voice="nova",
  input=text) as response:
  response.stream_to_file(speech_file_path)