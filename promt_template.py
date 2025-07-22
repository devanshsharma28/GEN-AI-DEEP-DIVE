from langchain_ollama.chat_models import ChatOllama

from langchain.prompts import PromptTemplate

promt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question: {question}",
)

llm = ChatOllama(model="llama3.2:latest")

chain = promt | llm #Chain

response = chain.invoke({"question": "Who invented Agni (missile)"})

print(response.content)