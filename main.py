# from langchain_ollama import OllamaLLM

# model = OllamaLLM(model="llama3.2")

# result = model.invoke(input="write a poem on moon like 5 lines")
# print(result)

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template ="""
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context =""
    print("Welcome to the AI ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        result = chain.invoke({"context":context,"question":user_input})
        print("Bot:",result)
        context += f"\nUser:{user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()