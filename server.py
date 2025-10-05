# server.py
# https://github.com/jlowin/fastmcp
from fastmcp import FastMCP

mcp = FastMCP("add-mcp-http")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

