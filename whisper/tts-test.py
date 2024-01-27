from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="onyx",
  input="Hallo, ich finde du bist echt etwas chaotisch. Aber ich mag dich!")

response.stream_to_file(speech_file_path)