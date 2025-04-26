# =============================================================================
# BigBrain — Configuration Logic & Conflict Detection
# Applies undo settings reading from preferences.edit and
# populates utils.conflicts list.
# =============================================================================

import bpy
from . import utils

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
    # Detect conflicts at startup
    try:
        utils.conflicts = utils.detect_conflicts()
    except Exception as e:
        print(f"[BigBrain] Conflict detection failed: {e}")

def unregister():
    pass
