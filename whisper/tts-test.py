from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
with open(Path(__file__).parent / "transcript.txt", "r") as file:
  input_text = file.read()

with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="onyx",
  input=input_text) as response:
  response.stream_to_file(speech_file_path)