# =============================================================================
# BigBrain Addon for Blender
# Author: github@DctrXD
# Version: 2.0.0
# Supported: Blender 2.93+ (tested on 3.x, 4.x)
# =============================================================================

bl_info = {
    "name": "BigBrain",
    "author": "github@DctrXD",
    "version": (2, 0, 0),  # Atualizado para versão 2.0.0
    "blender": (2, 93, 0),
    "location": "View3D Header & Sidebar",
    "description": "Infinite undo + RAM status bar & overlay + log viewer + i18n + conflict detection + reset",
    "warning": "",
    "doc_url": "https://github.com/DctrXD",
    "category": "System",
}

import importlib
import bpy
from . import config, preferences, utils, operators, ui, i18n, version

# All modules to reload on register
modules = [i18n, config, preferences, utils, operators, ui, version]

def _validate_blender_version():
    if bpy.app.version < bl_info["blender"]:
        print(f"[BigBrain] Warning: Blender {bpy.app.version_string} < {bl_info['blender']}, some features may not work.")
    
    # Verificação específica para Blender 4.0+
    if bpy.app.version >= (4, 0, 0):
        print(f"[BigBrain] Running on Blender {bpy.app.version_string} - Using Blender 4.0+ compatibility mode")

def register():
    _validate_blender_version()
    
    # Register all modules
    for m in modules:
        importlib.reload(m)
        m.register()
    
    # Apply settings after all modules are registered
    config.apply_undo_settings()
    
    # Log successful registration
    utils.log(f"BigBrain v{'.'.join(str(v) for v in bl_info['version'])} registered successfully")

def unregister():
    # Stop RAM monitoring before unregistering
    utils.ram_monitor.stop_ram_status()
    
    # Unregister all modules in reverse order
    for m in reversed(modules):
        m.unregister()
    
    # Log unregistration
    print("[BigBrain] Addon unregistered")

# Allow running the script directly from Blender's text editor
if __name__ == "__main__":
    register()
