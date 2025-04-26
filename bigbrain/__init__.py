# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 1.2.3
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 2, 3),
    "blender": (2, 93, 0),
    "location": "View3D Header & Sidebar",
    "description": "Infinite undo + RAM status bar & overlay + log viewer + i18n + conflict detection + reset",
    "warning": "",
    "doc_url": "https://github.com/DctrXD",
    "category": "System",
}

import importlib, bpy
from . import config, preferences, utils

modules = [config, preferences, utils]

def _validate_blender_version():
    if bpy.app.version < bl_info["blender"]:
        print(f"[BigBrain] Warning: Blender {bpy.app.version_string} < {bl_info['blender']}, some features may not work.")

def register():
    _validate_blender_version()
    for m in modules:
        importlib.reload(m)
        m.register()
    config.apply_undo_settings()
    utils.start_ram_status()

def unregister():
    utils.stop_ram_status()
    for m in reversed(modules):
        m.unregister()
