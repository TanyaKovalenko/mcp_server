from fastmcp import FastMCP
import envs

mcp_server = FastMCP(
    name="SimpleMCPServer",
)

@mcp_server.tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

@mcp_server.tool
def author_favorite_color(a: int) -> str:
    """Says the author's favorite color."""
    if a == 1:
        return "Blue"
    elif a == 2:
        return "Red"
    else:
        return "Unknown"


def main():
    mcp_server.run(transport="http", host=envs.MCP_HOST, port=envs.MCP_PORT)

if __name__ == "__main__":
    main()