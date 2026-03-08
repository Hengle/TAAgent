"""
Material Tools for Unreal Render MCP

Material graph building and analysis tools.
"""

from typing import Dict, Any, List, Optional
import logging

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import send_command, save_json_to_file, with_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


@with_unreal_connection
def build_material_graph(
    material_name: str,
    nodes: List[Dict[str, Any]],
    connections: List[Dict[str, Any]] = None,
    properties: Dict[str, Any] = None,
    compile: bool = True
) -> Dict[str, Any]:
    """
    Build an entire material graph in a single call (batch operation).
    
    Args:
        material_name: Name or path of the material (must already exist)
        nodes: List of node definitions
        connections: List of connection definitions
        properties: Optional material properties to set
        compile: Whether to compile the material after building
    """
    params = {
        "material_name": material_name,
        "nodes": nodes,
        "compile": compile
    }
    if connections:
        params["connections"] = connections
    if properties:
        params["properties"] = properties
    
    return send_command("build_material_graph", params)


@with_unreal_connection
def compile_material(material_name: str) -> Dict[str, Any]:
    """Compile a material to update its shader."""
    return send_command("compile_material", {"material_name": material_name})


@with_unreal_connection
def get_material_graph(material_name: str, save_to: Optional[str] = None) -> Dict[str, Any]:
    """
    Get complete material graph including nodes and connections.
    
    Args:
        material_name: Name or path of the material
        save_to: Optional path to save JSON
    """
    result = send_command("get_material_graph", {"material_name": material_name})
    
    if save_to and result.get("success"):
        save_info = save_json_to_file(result, save_to, "material_graph", material_name)
        result.update(save_info)
    
    return result


@with_unreal_connection
def get_material_function_content(function_path: str, save_to: Optional[str] = None) -> Dict[str, Any]:
    """
    Get detailed content of a Material Function.
    
    Args:
        function_path: Full path to the Material Function
        save_to: Optional path to save JSON
    """
    result = send_command("get_material_function_content", {"function_path": function_path})
    
    if save_to and result.get("success"):
        func_name = function_path.split("/")[-1].split(".")[0]
        save_info = save_json_to_file(result, save_to, "material_function", func_name)
        result.update(save_info)
    
    return result
