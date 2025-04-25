# =============================================================================
# BigBrain — Configuration Logic
# Applies undo settings reading from preferences.edit
# =============================================================================

import bpy

def apply_undo_settings():
    """🇬🇧 Safely apply undo settings. 🇧🇷 Aplica desfazer com segurança."""
    prefs = bpy.context.preferences.edit
    addon_prefs = bpy.context.preferences.addons[__package__].preferences

    # Undo Steps
    try:
        prefs.undo_steps = addon_prefs.undo_steps
    except Exception as e:
        print(f"[BigBrain] Could not set undo_steps: {e}")

    # Undo Memory Limit
    try:
        prefs.undo_memory_limit = addon_prefs.undo_memory_limit
    except Exception as e:
        print(f"[BigBrain] Could not set undo_memory_limit: {e}")

def register():
    pass  # no-op

def unregister():
    pass
