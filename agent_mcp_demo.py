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

from veadk import Agent, Runner
from veadk.memory.short_term_memory import ShortTermMemory
from veadk.utils.logger import get_logger
from veadk.utils.mcp_utils import get_mcp_params
from veadk.tools.mcp_tool.trusted_mcp_toolset import TrustedMcpToolset

logger = get_logger(__name__)
logger.level = "DEBUG"

# import os
# os.environ["MODEL_AGENT_NAME"] = "doubao-seed-1-6-251015"  # <-- 火山方舟大模型名称
# os.environ["MODEL_AGENT_API_KEY"] = os.getenv("PPE_API_KEY", "")  # <-- 设置火山方舟的API KEY来访问模型
# os.environ["LOGGING_LEVEL"] = "DEBUG"  # <-- 调整日志等级
# 设置火山引擎 AK 和 SK 来使用 web_search 工具
# os.environ["VOLCENGINE_ACCESS_KEY"] = os.getenv("PPE_AK", "")
# os.environ["VOLCENGINE_SECRET_KEY"] = os.getenv("PPE_SK", "")


async def main():
    app_name = "veadk_playground_app"
    user_id = "veadk_playground_user"
    session_id = "veadk_playground_session"
    mcp_url = "http://127.0.0.1:8000/mcp"
    mcp_url = "http://101.126.65.161:8000/mcp"

    # 通过 fastmcp 客户端获取 MCP 工具列表
    # from fastmcp import Client
    # async with Client(mcp_url) as client:
    #     mcp_tools = await client.list_tools()
    #     print(mcp_tools)

    # # 通过 trustedmcp 客户端获取 TrustedMCP 工具列表
    # from bytedance.jeddak_trusted_mcp import trusted_mcp_client as TrustedClient
    # # aicc_config_path = "./aicc_config.json"
    # async with TrustedClient(url=mcp_url) as client:
    #     mcp_tools = await client.list_tools()
    #     print(mcp_tools)

    # 初始化 McpToolset 工具集
    connection_params = get_mcp_params(mcp_url)
    # 开启 TrustedMCP 功能以及相关配置
    connection_params.headers = {"x-trusted-mcp": "true"}
    # connection_params.headers = {"x-trusted-mcp": "true", "aicc-config": "./aicc_config.json"}
    # 配置文件内容请参见[TrustedMCP 配置文件](https://github.com/volcengine/AICC-Trusted-MCP/blob/main/README.md)
    # toolset = McpToolset(connection_params=connection_params)
    toolset = TrustedMcpToolset(connection_params=connection_params)
    # 初始化 VeIdentityMcpToolset 工具集
    # from veadk.integrations.ve_identity import VeIdentityMcpToolset, api_key_auth
    # toolset = VeIdentityMcpToolset(
    #     auth_config=api_key_auth("volc"),
    #     connection_params=get_mcp_params(mcp_url, os.getenv("PPE_API_KEY", "")),
    # )

    # 初始化 Agent 并添加工具
    agent = Agent(tools=[toolset])
    # from veadk.tools.builtin_tools.web_search import web_search
    # from veadk.tools.demo_tools import get_city_weather
    # agent = Agent(tools=[toolset] if toolset else [web_search, get_city_weather])

    # 初始化 Runner
    runner = Runner(
        agent=agent,
        short_term_memory=ShortTermMemory(),
        app_name=app_name,
        user_id=user_id,
    )

    # 运行 Agent
    message = "成都今天的天气"
    response = await runner.run(messages=message, session_id=session_id)
    print(f"message: {message}, response: {response}")

    # message = "北京今天的空气质量"
    # response = await runner.run(messages=message, session_id=session_id)
    # print(f"message: {message}, response: {response}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
