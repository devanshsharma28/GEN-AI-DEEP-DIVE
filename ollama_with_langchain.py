from langchain_ollama.chat_models import ChatOllama

llm = ChatOllama(model="llama3.2:latest")

response = llm.invoke("What is captial of Russia?")

print(response.content)