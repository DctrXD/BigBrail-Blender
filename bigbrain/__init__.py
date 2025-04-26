# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 1.1.0
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# Summary: Registers modules, validates version, applies undo settings.
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 1, 0),
    "blender": (2, 93, 0),
    "location": "Edit > Preferences > Add-ons",
    "description": "Unlocks near-infinite Ctrl+Z history with real-time RAM graph, multi-lang UI, conflict detection and reset button",
    "warning": "",
    "doc_url": "https://github.com/DctrXD",
    "category": "System",
}

import importlib
import bpy

from . import config, preferences, utils

modules = [config, preferences, utils]

def register():
    # Version validation
    ver = bpy.app.version
    if ver < bl_info["blender"]:
        print(f"[BigBrain] Warning: Blender version {ver} < {bl_info['blender']}, some features may not work.")
    # Reload & register modules
    for m in modules:
        importlib.reload(m)
        m.register()
    config.apply_undo_settings()

def unregister():
    for m in reversed(modules):
        m.unregister()
