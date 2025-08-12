from fastmcp import FastMCP
from datetime import datetime
import pytz
import envs

mcp_server = FastMCP(
    name="SimpleMCPServer",
)

@mcp_server.tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

@mcp_server.tool
def moscow_time(a: int) -> str:
    """Returns the current time in Moscow."""
    return datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')


def main():
    mcp_server.run(transport="http", host=envs.MCP_HOST, port=envs.MCP_PORT)

if __name__ == "__main__":
    main()