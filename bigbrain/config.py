# =============================================================================
# Infinite Undo - Configuration Logic
# Author: github@DctrXD
# Summary: Applies undo settings based on user preferences.
# =============================================================================

import bpy

def apply_undo_settings():
    # Applies the user's undo config from addon preferences
    # Aplica as configurações de desfazer definidas pelo usuário
    addon_prefs = bpy.context.preferences.addons[__package__].preferences
    prefs = bpy.context.preferences.system

    prefs.undo_steps = addon_prefs.undo_steps
    prefs.undo_memory_limit = addon_prefs.undo_memory_limit

def register():
    pass  # Nothing to register here yet

def unregister():
    pass
