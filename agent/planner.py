import json
from agent.llm import ask_llm

def is_dockerfile_request(user_input: str) -> bool:
    keywords = ["dockerfile", "containerize", "docker image", "docker build"]
    return any(k in user_input.lower() for k in keywords)

def plan_devops_action(user_input: str):
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
        return parsed["steps"], parsed.get("container")
    except Exception:
        return [], None
