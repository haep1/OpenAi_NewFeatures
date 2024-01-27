from openai import OpenAI
client = OpenAI()
#print(openai.Model.list())
#result = openai.Completion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

testPrompt="""
Extrahiere aus dem folgenden Text mögliche Suchbegriffe, die den Sachverhalt eindeutig widerspiegeln. Konzentriere dich auf Fachbegriffe. Antworte nur in Json mit maximal 5 Begriffen. Beispiel: {"Suchbegriffe": ["Klageerwiderung", "Klageantwort", "Klageantwortfrist"]}
Der Text lautet: 
Die Klägerin war seit mehreren Jahren Mitglied des sozialen Netzwerks der Beklagten und hatte dort 
ein persönliches Benutzerkonto mit verschiedenen Profilinformationen, darunter ihren vollständigen 
Namen, Geburtsdatum, Adresse, Telefonnummer und E-Mail-Adresse.
Am 14. Dezember 2022 wurde das soziale Netzwerk der Beklagten Opfer eines schwerwiegenden 
Hackerangriffs. Unbefugte Dritte drangen in die Systeme der Beklagten ein und griffen auf die 
Benutzerdatenbank zu. Dabei griffen Sie auch auf die persönlichen Daten von Bertha Schreiner zu
und kopierten diese.
Die Beklagte erkannte den Hackerangriff erst mehrere Tage später und stoppte den Zugriff. Sie 
unterrichtete die Nutzer wie auch die Datenschutz-Behörden.
"""

result = client.completions.create(model="gpt-3.5-turbo-instruct",
prompt = testPrompt,
#temperature=0.1,
max_tokens=1000)
print(result)