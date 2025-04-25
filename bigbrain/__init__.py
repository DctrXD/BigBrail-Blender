# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 1.0.1
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# Summary: Registers modules and applies undo settings safely.
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 0, 1),
    "blender": (2, 93, 0),
    "location": "Edit > Preferences > Add-ons",
    "description": "Unlocks near-infinite Ctrl+Z history with custom undo steps & memory limits",
    "warning": "",
    "doc_url": "https://github.com/SEU_USUARIO/BigBrain",
    "category": "System",
}

import importlib
import bpy

from . import config, preferences, utils

modules = [config, preferences, utils]

def register():
    for m in modules:
        importlib.reload(m)
        m.register()
    config.apply_undo_settings()

def unregister():
    for m in reversed(modules):
        m.unregister()
