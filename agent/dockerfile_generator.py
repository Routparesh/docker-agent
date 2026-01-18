from agent.llm import ask_llm

def generate_dockerfile(app_type: str, port: str, start_cmd: str = None):
    prompt = f"""
Generate a PRODUCTION-READY Dockerfile.

Rules:
- Use multi-stage build if applicable
- Use non-root user
- Small image size
- Expose correct port
- No explanations
- ONLY Dockerfile content

App Type: {app_type}
Port: {port}
Start Command: {start_cmd or "auto-detect"}
"""
    return ask_llm(prompt)
