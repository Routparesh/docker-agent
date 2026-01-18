import ollama

MODEL = "llama3.2:3b"

def ask_llm(prompt: str) -> str:
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a senior DevOps engineer."},
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2,
            "num_ctx": 4096
        }
    )
    return response["message"]["content"].strip()
