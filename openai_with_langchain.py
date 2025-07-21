from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("What is capital of Russia?")
print(response.content)