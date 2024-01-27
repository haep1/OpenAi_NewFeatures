from openai import OpenAI
client = OpenAI()

functions= [  
    {
        "name": "find_cases",
        "description": "Finds all cases based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "max_dispute": {
                    "type": "number",
                    "description": "The maximum dispute value for the case"
                },
                "min_dispute": {
                    "type": "number",
                    "description": "The minimum dispute value for the case"
                },
                "has_lawsuit": {
                    "type": "boolean",
                    "description": "Is true if the case has a pending lawsuit"
                },
                "has_judgement": {
                    "type": "boolean",
                    "description": "Is true if a judgment for this case has been rendered"
                },
                "clerk": {
                    "type": "string",
                    "description": "The clerk of the case"
                },
                "participants": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the participant"
                            },
                            "type": {
                                "type": "string",
                                "description": "The type of the participant"
                            }
                        }
                    }
                }
            },
            "required": ["has_lawsuit", "has_judgement"]
        }
    },
    {
        "name": "create_case",
        "description": "Creates a new case",
        "parameters": {
            "type": "object",
            "properties": {
                "dispute": {
                    "type": "number",
                    "description": "The maximum dispute value for the case"
                },
                "clerk": {
                    "type": "string",
                    "description": "The clerk of the case"
                },
                "participants": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The name of the participant"
                            },
                            "type": {
                                "type": "string",
                                "description": "The type of the participant"
                            }
                        }
                    }
                }
            }
        }
    },
    #Ergänze um eine Funktion, die uns allen eine Pizza bestellt und eine, die uns alle in den Urlaub schickt.
    {
        "name": "order_pizza",
        "description": "Orders pizza for everyone",
        "parameters": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "The type of pizza"
                },
                "size": {
                    "type": "string",
                    "description": "The size of the pizza"
                },
                "toppings": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "The toppings of the pizza"
                    }
                }
            }
        }
    },
    {
        "name": "send_everyone_on_vacation",
        "description": "Sends everyone on vacation",
        "parameters": {
            "type": "object",
            "properties": {
                "destination": {
                    "type": "string",
                    "description": "The destination of the vacation"
                },
                "duration": {
                    "type": "string",
                    "description": "The duration of the vacation"
                }
            }
        }
    }
]  

#question = "Finde alle Akten, in denen Franz Huber Sachbearbeiter ist."
#question = "Finde alle Akten im anhängigen Verfahren am Landgericht München mit einem Streitwert zwischen 2000€ und 10000€, mit der Social Media AG als Gegner und der Massive Attack als Mandant."
question = "Lege eine neue Akte Social Media AG ./. Massive Attack mit einem Streitwert von 5000€ an und weise sie Franz Huber als Sachbearbeiter zu."

messages= [
    {"role": "user", "content": question + 
     '''
     ###
     The court is a participant too. Possible participant types are: oponent, mandant, court, lawfirm.'''}
]

response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=messages,
functions=functions,
function_call="auto")

print(response.choices[0].message)