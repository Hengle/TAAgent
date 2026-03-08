"""
Unreal MCP Common Utilities

Shared utilities for all tool modules.
"""

import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from functools import wraps

from connection import get_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


def save_json_to_file(
    data: Dict[str, Any],
    save_to: str,
    tool_name: str,
    asset_name: str = None
) -> Dict[str, Any]:
    """
    Save JSON data to a local file.
    
    Args:
        data: The JSON data to save
        save_to: Either a directory path or a full file path
        tool_name: Name of the calling tool (for auto-naming)
        asset_name: Optional asset name (for auto-naming)
    
    Returns:
        Dict with save status info, or empty dict if save_to is None
    """
    if not save_to:
        return {}
    
    try:
        save_path = Path(save_to)
        
        # If it's a directory, auto-generate filename
        if save_to.endswith('/') or save_to.endswith('\\') or save_path.is_dir():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_asset_name = (asset_name or "data").replace('/', '_').replace('\\', '_')
            filename = f"{tool_name}_{safe_asset_name}_{timestamp}.json"
            save_path = save_path / filename
        
        # Create parent directories
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write JSON
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved JSON to: {save_path}")
        return {
            "saved_to": str(save_path.absolute()),
            "save_success": True
        }
    
    except Exception as e:
        logger.error(f"Failed to save JSON: {e}")
        return {
            "save_success": False,
            "save_error": str(e)
        }


def with_unreal_connection(func):
    """
    Decorator to handle connection and error handling for MCP tools.
    Preserves function signature for FastMCP introspection.
    
    Usage:
        @with_unreal_connection
        def my_tool(param: str) -> Dict[str, Any]:
            return {"param": param}
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{func.__name__} error: {e}")
            return {"success": False, "message": str(e)}
    return wrapper


def send_command(command: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Send a command to Unreal Engine and return the response.
    
    Args:
        command: Command name
        params: Command parameters
        
    Returns:
        Response dict or error dict
    """
    unreal = get_unreal_connection()
    response = unreal.send_command(command, params)
    return response or {"success": False, "message": "No response from Unreal"}
