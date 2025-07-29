import openai
import os
from openai import OpenAI

key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

messages = []

client = OpenAI(
    api_key = key,
)

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })

    chat_completion = client.chat.completions.create(messages = messages,
                                                    model="gpt-4o"
                                                    )
    messages = {
        "role":"assistant",
        "content":chat_application.choices[0].messages.content   
    }
    messages.append(message)
    print(f"Jarvis:hi A am Jarvis,how may I help you\n")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis ,How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)