"""
Mesh Tools for Unreal Render MCP

Mesh import and creation tools.
"""

from typing import Dict, Any, List, Optional
import logging

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import send_command, with_unreal_connection

logger = logging.getLogger("UnrealRenderMCP")


@with_unreal_connection
def import_fbx(
    fbx_path: str,
    destination_path: str = "/Game/ImportedMeshes/",
    asset_name: str = None,
    spawn_in_level: bool = True,
    location: List[float] = None
) -> Dict[str, Any]:
    """
    Import an FBX file into Unreal Engine and optionally spawn it in the level.

    Args:
        fbx_path: Absolute path to the FBX file
        destination_path: Destination path in Unreal
        asset_name: Name for the imported asset
        spawn_in_level: Whether to spawn the mesh in the level
        location: Spawn location [x, y, z]
    """
    params = {
        "fbx_path": fbx_path,
        "destination_path": destination_path,
        "spawn_in_level": spawn_in_level,
    }
    if asset_name is not None:
        params["asset_name"] = asset_name
    if location is not None:
        params["location"] = location

    return send_command("import_fbx", params)


@with_unreal_connection
def create_static_mesh_from_data(
    name: str,
    positions: List[List[float]],
    indices: List[int],
    normals: List[List[float]] = None,
    uvs: List[List[float]] = None,
    tangents: List[List[float]] = None,
    colors: List[List[float]] = None,
    destination_path: str = "/Game/Meshes/",
    spawn_in_level: bool = True,
    location: List[float] = None
) -> Dict[str, Any]:
    """
    Create a static mesh directly from vertex data (bypasses FBX import).
    
    Args:
        name: Name for the new static mesh
        positions: List of vertex positions [[x,y,z], ...]
        indices: List of triangle indices (3 per triangle)
        normals: Optional list of vertex normals
        uvs: Optional list of UV coordinates
        tangents: Optional list of tangents
        colors: Optional list of vertex colors
        destination_path: Destination path in Unreal
        spawn_in_level: Whether to spawn the mesh in the level
        location: Spawn location [x, y, z]
    """
    params = {
        "name": name,
        "positions": positions,
        "indices": indices,
        "destination_path": destination_path,
        "spawn_in_level": spawn_in_level
    }
    if normals is not None:
        params["normals"] = normals
    if uvs is not None:
        params["uvs"] = uvs
    if tangents is not None:
        params["tangents"] = tangents
    if colors is not None:
        params["colors"] = colors
    if location is not None:
        params["location"] = location
    
    return send_command("create_static_mesh_from_data", params)
