from openai import OpenAI

client = OpenAI()
f = open("/Users/haep/Dev/Python/openAI_TTS_Covid19Urteile.mp3", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1", file=f)
print(transcript)