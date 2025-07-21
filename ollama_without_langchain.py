import ollama

response = ollama.chat(
    model='llama3.2:latest',
    messages=[
       {"role": "user", "content": "What is Captial of France"},
    ])

print(response["message"]["content"])