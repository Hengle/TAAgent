"""
TA Agent - 技术美术智能助手

TA Agent 是具备专业 TA 能力的智能代理，能够：
- 分析渲染问题
- 重建材质资产
- 优化性能瓶颈
- 自动化工作流

MCP 是 Agent 用来"改变世界"的工具。
"""

from .reasoning.problem_decomposer import decompose, analyze, ProblemType, Priority
from .reasoning.tool_selector import (
    select_tools_for_task,
    select_mcp_for_workflow,
    list_available_mcps,
    MCP_REGISTRY
)

__all__ = [
    # 问题分解
    "decompose",
    "analyze",
    "ProblemType",
    "Priority",
    # 工具选择
    "select_tools_for_task",
    "select_mcp_for_workflow",
    "list_available_mcps",
    "MCP_REGISTRY",
]
