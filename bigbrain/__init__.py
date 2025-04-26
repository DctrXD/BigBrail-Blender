# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 1.1.2
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 1, 2),
    "blender": (2, 93, 0),
    "location": "Edit > Preferences > Add-ons",
    "description": "Infinite undo + RAM status bar + log viewer + i18n + conflict detection + reset",
    "doc_url": "https://github.com/DctrXD",
    "category": "System",
}

import importlib
import bpy
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
