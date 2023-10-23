from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import openai
import json

with open("gpt-creds.json", "r") as file:
    access_key = json.load(file)

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
model = ChatOpenAI(openai_api_key=access_key["api_key"], model="gpt-3.5-turbo-instruct")
chain = prompt | model

print(chain.invoke({"foo": "bears"}))