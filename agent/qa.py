from agent.llm import ask_llm

def answer_question(user_input: str) -> str:
    prompt = f"""
You are a DevOps expert.
Answer the following question clearly and concisely.

Question:
{user_input}
"""
    return ask_llm(prompt)
