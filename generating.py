from globals import *
import ollama

def local(model: str, quest: list[dict]):
    if model == free[0]:
        return gptbaby(quest)
    else:
        return localized(model, quest)
    
def resgenerator(model: str, quest: list[dict]):
    completions = client.chat.completions.create(
        model=model,
        messages=quest
    )
    return completions.choices[0].message.content + " \n"

def gptbaby(quest: list[dict]):
    completions = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=quest 
    )
    return completions.choices[0].message.content + " \n"

def localized(model: str, quest: list[dict]):
    response = ollama.chat(
    model=model,
    messages=quest
    )
    return response['message']['content'] + "\n"

def shorted(quest: str):
    return quest + " Keep the response less than 5 sentences. "

def med(quest: str):
    return quest + " Keep the response less than 10 sentences. "
    