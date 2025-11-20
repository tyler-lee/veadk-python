# server.py
import os
from fastmcp import FastMCP
from typing import Any
from veadk.tools.builtin_tools.web_search import web_search
from veadk.tools.demo_tools import get_city_weather

os.environ["VOLCENGINE_ACCESS_KEY"] = os.getenv("PPE_AK", "")
os.environ["VOLCENGINE_SECRET_KEY"] = os.getenv("PPE_SK", "")

mcp = FastMCP("🚀 Mock Remote MCP Server 🚀")


@mcp.tool
def mcp_add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool
def mcp_web_search(query: str, tool_context: Any | None = None) -> list[str]:
    """Search a query in websites.

    Args:
        query: The query to search.

    Returns:
        A list of result documents.
    """
    return web_search(query, tool_context)


@mcp.tool
def mcp_get_city_weather(city: str) -> dict[str, str]:
    """Retrieves the weather information of a given city. the args must in English"""
    return get_city_weather(city)


if __name__ == "__main__":
    # Start an HTTP server on port 8000
    mcp.run(transport="http", host="127.0.0.1", port=8000)

# fastmcp run server.py
