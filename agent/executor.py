from datetime import datetime
from mcp.client import DockerMCP

docker = DockerMCP()

def execute(steps, container=None):
    results = []
    for step in steps:
        res = docker.call(step, {"container": container} if container else {})
        results.append(res)

        with open("logs/audit.log", "a") as log:
            log.write(f"{datetime.utcnow()} | {step} | {container}\n")

    return results
