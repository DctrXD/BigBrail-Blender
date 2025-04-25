# =============================================================================
# Infinite Undo Addon for Blender
# Author: github@DctrXD
# Summary: Entry point. Registers and initializes the addon.
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "Edit > Preferences > Add-ons",
    "description": "Expande os limites de desfazer no Blender (Ctrl+Z quase infinito)",
    "category": "System",
}

import importlib
import bpy

# Modular import: reload for development
from . import config, preferences, utils

modules = [config, preferences, utils]
for m in modules:
    importlib.reload(m)

def register():
    for m in modules:
        m.register()
    config.apply_undo_settings()

def unregister():
    for m in reversed(modules):
        m.unregister()
