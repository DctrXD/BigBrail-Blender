# =============================================================================
# BigBrain — Configuration Logic & Conflict Detection
# Applies undo settings reading from preferences.edit.
# =============================================================================

import bpy
from . import utils

def apply_undo_settings():
    """Apply undo_steps & undo_memory_limit safely."""
    prefs = bpy.context.preferences.edit
    addon_prefs = bpy.context.preferences.addons["bigbrain"].preferences

    try:
        prefs.undo_steps = addon_prefs.undo_steps
    except Exception as e:
        print(f"[BigBrain] Failed to set undo_steps: {e}")
    try:
        prefs.undo_memory_limit = addon_prefs.undo_memory_limit
    except Exception as e:
        print(f"[BigBrain] Failed to set undo_memory_limit: {e}")

def register():
    # detect conflicts on startup
    try:
        utils.conflicts = utils.detect_conflicts()
    except Exception as e:
        print(f"[BigBrain] Conflict detection error: {e}")

def unregister():
    pass
