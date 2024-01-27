import openai

testPrompt="""
Wieviele Wochen nach Zustellung der Klageschrift ist die Klageerwiderung fällig? Zähle wenn nötig die Fristen zusammen und beziehe dich bei der Dauer immer auf die Zustellung der Klageschrift. Antworte nur in Json.
Beispiel: {"Frist": "3 Wochen",
          "Begründung": "Hier kommt die Begründung hin"}

Der Text lautet: die beklagte Partei ergehen gemäß § 276 ZPO folgende Aufforderungen: 
2.1. Die beklagte Partei hat die Absicht der Verteidigung binnen einer 
Notfrist von zwei Wochen
ab Zustellung der Klageschrift durch ihren Rechtsanwalt schriftlich anzuzeigen. 
Belehrungen:
Die Frist kann nicht verlängert werden und ist nur dann gewahrt, wenn die Anzeige 
innerhalb der Frist bei Gericht eingeht. Geht sie nicht innerhalb der Frist ein, kann dies 
zu einem Verlust des Prozesses führen. Das Gericht kann auf Antrag der Gegenpartei
ein Versäumnisurteil erlassen (§ 331 ZPO); in diesem Fall hat die säumige Partei auch 
die Gerichtskosten und die notwendigen Auslagen der Gegenseite zu tragen 
(§ 91 ZPO). Aus dem Versäumnisurteil kann der Gegner der säumigen Partei gegen 
diese die Zwangsvollstreckung betreiben (§ 708 Nr. 2 ZPO).
Erklärt die Beklagtenpartei, dass sie den Klageanspruch ganz oder teilweise 
anerkenne, so wird sie ohne mündliche Verhandlung dem Anerkenntnis gemäß 
verurteilt werden.
2.2. Sie hat auf das Klagevorbringen innerhalb von 2 Wochen nach Ablauf der oben genannten Notfrist schriftlich zu erwidern, wenn sie sich gegen 
die Klage verteidigen will. Dabei soll auch erklärt werden, ob einer Entscheidung der 
Sache durch den Einzelrichter Gründe entgegen stehen
"""

result = openai.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt = testPrompt,
  #temperature=0.1,
  max_tokens=1000,
  #top_p=1,
  #frequency_penalty=0.0,
  #presence_penalty=0.6,
  #stream=True
)
print(result)