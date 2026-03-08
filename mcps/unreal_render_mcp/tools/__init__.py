"""
Unreal Render MCP Tools

Modular tool definitions for Unreal Engine operations.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from material import (
    build_material_graph,
    compile_material,
    get_material_graph,
    get_material_function_content,
)

from texture import (
    import_texture,
    set_texture_properties,
)

from mesh import (
    import_fbx,
    create_static_mesh_from_data,
)

from actor import (
    spawn_actor,
    delete_actor,
    get_actors,
    set_actor_properties,
    get_actor_properties,
    batch_spawn_actors,
    batch_delete_actors,
    batch_set_actors_properties,
)

from asset import (
    create_asset,
    delete_asset,
    set_asset_properties,
    get_asset_properties,
    get_assets,
    batch_create_assets,
    batch_set_assets_properties,
)

from niagara import (
    get_niagara_asset_details,
    update_niagara_asset,
    analyze_stateless_compatibility,
    convert_to_stateless,
    get_niagara_module_graph,
    get_niagara_script_asset,
    update_niagara_script_asset,
)

from viewport import (
    get_viewport_screenshot,
)

__all__ = [
    # Material
    "build_material_graph",
    "compile_material",
    "get_material_graph",
    "get_material_function_content",
    # Texture
    "import_texture",
    "set_texture_properties",
    # Mesh
    "import_fbx",
    "create_static_mesh_from_data",
    # Actor
    "spawn_actor",
    "delete_actor",
    "get_actors",
    "set_actor_properties",
    "get_actor_properties",
    "batch_spawn_actors",
    "batch_delete_actors",
    "batch_set_actors_properties",
    # Asset
    "create_asset",
    "delete_asset",
    "set_asset_properties",
    "get_asset_properties",
    "get_assets",
    "batch_create_assets",
    "batch_set_assets_properties",
    # Niagara
    "get_niagara_asset_details",
    "update_niagara_asset",
    "analyze_stateless_compatibility",
    "convert_to_stateless",
    "get_niagara_module_graph",
    "get_niagara_script_asset",
    "update_niagara_script_asset",
    # Viewport
    "get_viewport_screenshot",
]
