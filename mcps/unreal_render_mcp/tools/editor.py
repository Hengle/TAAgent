"""
Editor Tools for Unreal Render MCP

Level management and editor operations.
"""

from typing import Dict, Any, Optional
import logging

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import send_command, with_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


@with_unreal_connection
def create_level(level_path: str) -> Dict[str, Any]:
    """
    Create a new level and save it to the specified path.
    
    Args:
        level_path: Path to save the level (e.g., "/Game/Levels/LookDev")
    
    Returns:
        Success status and level path
    """
    return send_command("create_level", {"level_path": level_path})


@with_unreal_connection
def load_level(level_path: str) -> Dict[str, Any]:
    """
    Load an existing level.
    
    Args:
        level_path: Path to the level (e.g., "/Game/Levels/LookDev")
    
    Returns:
        Success status and level path
    """
    return send_command("load_level", {"level_path": level_path})


@with_unreal_connection
def save_current_level() -> Dict[str, Any]:
    """
    Save the current level.
    
    Returns:
        Success status
    """
    return send_command("save_current_level", {})


@with_unreal_connection
def get_current_level() -> Dict[str, Any]:
    """
    Get information about the current level.
    
    Returns:
        Level name and path
    """
    return send_command("get_current_level", {})