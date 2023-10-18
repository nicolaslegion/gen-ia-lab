import json
import openai

with open("gpt-creds.json", "r") as file:
    access_key = json.load(file)

openai.api_key = access_key["api_key"]
model="gpt-3.5-turbo-instruct"#gpt-3.5-turbo"

class Bot:
    def __init__(self):
        self.name = "NicoGPT"

    def respond(self, user_input):
        gpt_response = openai.Completion.create(model=model, prompt=user_input, temperature=0.9, max_tokens=150)["choices"][0]["text"]
        return f'{self.name}: {gpt_response}'

class ChatSession:
    def __init__(self, bot):
        self.bot = bot

    def start(self):
        print("Welcome to the chat session!")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            bot_response = self.bot.respond(user_input)
            print(bot_response)

if __name__ == "__main__":
    bot = Bot()
    chat_session = ChatSession(bot)
    chat_session.start()