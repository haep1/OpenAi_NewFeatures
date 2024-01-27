from openai import OpenAI

client = OpenAI()
#print(openai.Model.list())
#result = openai.Completion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

idea = "Indoor plant care reminder and tips app"
ideaPrompt = f"Write the basic python pseudocode for the idea: {idea}. only the pseudocode in python code. no other text"
testPrompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:"

result = client.completions.create(model="gpt-3.5-turbo-instruct",
prompt = ideaPrompt,
#temperature=0.9,
max_tokens=1000)
print(result)