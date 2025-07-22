from langchain_ollama.chat_models import ChatOllama

from langchain.prompts import ChatPromptTemplate

promt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Answer the following question: {question}"),    
])

llm = ChatOllama(model="llama3.2:latest")

chain = promt | llm

response = chain.invoke({"question": "Who invented Agni (missile)"})

print(response.content)