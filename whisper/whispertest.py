from pathlib import Path
from openai import OpenAI

client = OpenAI()
f = open(Path(__file__).parent / "openAI_TTS_Covid19Urteile.mp3", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1", file=f)
print(transcript)