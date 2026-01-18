from mcp_client import MCPClient

class DockerMCP:
    def __init__(self):
        self.client = MCPClient(
            server_url="http://localhost:3333",
            policy_file="config/policy.json"
        )

    def call(self, tool: str, args: dict = None):
        return self.client.call_tool(tool, args or {})
