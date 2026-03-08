"""
Niagara Tools for Unreal Render MCP

Niagara system analysis and modification tools.
"""

from typing import Dict, Any, List, Optional
import logging

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import send_command, save_json_to_file, with_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


@with_unreal_connection
def get_niagara_asset_details(
    asset_path: str,
    detail_level: str = "overview",
    emitters: List[str] = None,
    include: List[str] = None,
    save_to: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get detailed information about a Niagara system asset.
    
    Args:
        asset_path: Path to the Niagara system asset
        detail_level: Level of detail - "overview" or "full"
        emitters: Optional list of emitter names to filter
        include: Optional list of sections to include
        save_to: Optional path to save JSON
    """
    params = {
        "asset_path": asset_path,
        "detail_level": detail_level
    }
    if emitters is not None:
        params["emitters"] = emitters
    if include is not None:
        params["include"] = include
    
    result = send_command("get_niagara_asset_details", params)
    
    if save_to and result.get("success"):
        asset_name = result.get("asset_name", asset_path.split("/")[-1])
        save_info = save_json_to_file(result, save_to, "niagara_asset", asset_name)
        result.update(save_info)
    
    return result


@with_unreal_connection
def update_niagara_asset(
    asset_path: str,
    operations: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Batch update a Niagara system asset with multiple operations.
    
    Args:
        asset_path: Path to the Niagara system asset
        operations: List of operations to perform
    """
    return send_command("update_niagara_asset", {
        "asset_path": asset_path,
        "operations": operations
    })


@with_unreal_connection
def analyze_stateless_compatibility(
    asset_path: str,
    emitter: str
) -> Dict[str, Any]:
    """
    Analyze if a Standard Niagara emitter can be converted to Stateless mode.
    
    Args:
        asset_path: Path to the Niagara system asset
        emitter: Name of the emitter to analyze
    """
    return send_command("analyze_stateless_compatibility", {
        "asset_path": asset_path,
        "emitter": emitter
    })


@with_unreal_connection
def convert_to_stateless(
    asset_path: str,
    emitter: str,
    force: bool = False
) -> Dict[str, Any]:
    """
    Convert a Standard Niagara emitter to Stateless mode.
    
    Args:
        asset_path: Path to the Niagara system asset
        emitter: Name of the emitter to convert
        force: If True, attempt conversion even with warnings
    """
    return send_command("convert_to_stateless", {
        "asset_path": asset_path,
        "emitter": emitter,
        "force": force
    })


@with_unreal_connection
def get_niagara_module_graph(
    asset_path: str,
    emitter: str,
    script: str = "spawn",
    module: str = "",
    save_to: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get Niagara Module Graph nodes and connections.
    
    Args:
        asset_path: Path to the Niagara system asset
        emitter: Name of the emitter to inspect
        script: Script type - "spawn" or "update"
        module: Optional filter - only return nodes matching this module name
        save_to: Optional path to save JSON
    """
    params = {
        "asset_path": asset_path,
        "emitter": emitter,
        "script": script,
        "module": module
    }
    
    result = send_command("get_niagara_module_graph", params)
    
    if save_to and result.get("success"):
        graph_name = f"{emitter}_{script}"
        save_info = save_json_to_file(result, save_to, "niagara_graph", graph_name)
        result.update(save_info)
    
    return result


@with_unreal_connection
def get_niagara_script_asset(
    script_path: str,
    save_to: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get Niagara Script Asset details for standalone script assets.
    
    Args:
        script_path: Full path to the standalone Niagara Script asset
        save_to: Optional path to save JSON
    """
    result = send_command("get_niagara_script_asset", {"script_path": script_path})
    
    if save_to and result.get("success"):
        asset_name = result.get("script_name", script_path.split("/")[-1])
        save_info = save_json_to_file(result, save_to, "niagara_script", asset_name)
        result.update(save_info)
    
    return result


@with_unreal_connection
def update_niagara_script_asset(
    script_path: str,
    operations: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Update a standalone Niagara Script Asset.
    
    Args:
        script_path: Full path to a standalone Niagara Script asset
        operations: List of operations to perform
    """
    return send_command("update_niagara_script_asset", {
        "script_path": script_path,
        "operations": operations or []
    })
