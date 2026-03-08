"""
Viewport Tools for Unreal Render MCP

Viewport capture and screenshot tools.
"""

from typing import Dict, Any
import logging

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import send_command, with_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


@with_unreal_connection
def get_viewport_screenshot(
    output_path: str,
    format: str = "png",
    quality: int = 85,
    include_ui: bool = False
) -> Dict[str, Any]:
    """
    Capture a screenshot of the current viewport and save as image file.
    
    Args:
        output_path: Full path where to save the screenshot
        format: Image format - "png", "jpg", or "bmp"
        quality: JPEG quality 1-100 (only for jpg)
        include_ui: Whether to include editor UI
    """
    return send_command("get_viewport_screenshot", {
        "output_path": output_path,
        "format": format,
        "quality": quality,
        "include_ui": include_ui
    })
