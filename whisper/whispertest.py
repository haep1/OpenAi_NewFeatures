from pathlib import Path
from openai import OpenAI

client = OpenAI()
f = open(Path(__file__).parent / "output.wav", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1", file=f)
with open(Path(__file__).parent / "transcript.txt", "w") as file:
    file.write(transcript.text)