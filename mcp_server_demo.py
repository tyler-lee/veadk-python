# Copyright (c) 2025 Beijing Volcano Engine Technology Co., Ltd. and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
