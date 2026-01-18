import json
from agent.llm import ask_llm


# ONLY explicit generation requests should return True
def is_dockerfile_request(user_input: str) -> bool:
    explicit_phrases = [
        "generate dockerfile",
        "create dockerfile",
        "write dockerfile",
        "dockerfile for",
        "containerize app",
        "containerise app"
    ]

    text = user_input.lower().strip()
    return any(phrase in text for phrase in explicit_phrases)


def is_question(user_input: str) -> bool:
    question_words = ("what", "why", "where", "how", "when", "which")
    return user_input.lower().strip().startswith(question_words)


def plan_devops_action(user_input: str):
    # Guard: questions must never trigger actions
    if is_question(user_input):
        return [], None

    prompt = f"""
Convert the user request into Docker MCP steps.
Return ONLY valid JSON.

Allowed tools:
- docker_ps
- docker_logs
- docker_inspect
- docker_exec
- docker_run
- docker_stop

User request:
{user_input}

Format:
{{ "steps": ["tool1", "tool2"], "container": "name-or-null" }}
"""

    try:
        response = ask_llm(prompt)
        parsed = json.loads(response)
        return parsed.get("steps", []), parsed.get("container")
    except Exception:
        return [], None
