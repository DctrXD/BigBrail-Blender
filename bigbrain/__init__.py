# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 1.1.1
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# Summary: Registers modules, validates version, applies undo & RAM status.
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (1, 1, 1),
    "blender": (2, 93, 0),
    "location": "Edit > Preferences > Add-ons",
    "description": "Infinite undo + live RAM bar + i18n + conflict detection + reset",
    "warning": "",
    "doc_url": "https://github.com/SEU_USUARIO/BigBrain",
    "category": "System",
}

import importlib
import bpy

from . import config, preferences, utils

modules = [config, preferences, utils]

def _validate_blender_version():
    ver = bpy.app.version
    if ver < bl_info["blender"]:
        msg = (f"[BigBrain] Warning: Detected Blender {ver}, "
               f"but BigBrain requires ≥ {bl_info['blender']}.")
        print(msg)

def register():
    _validate_blender_version()
    for m in modules:
        importlib.reload(m)
        m.register()
    config.apply_undo_settings()
    utils.start_ram_status()  # inicia o timer de RAM

def unregister():
    utils.stop_ram_status()
    for m in reversed(modules):
        m.unregister()
