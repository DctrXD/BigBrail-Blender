# =============================================================================
# config.py — Applies undo prefs & detects conflicts
# =============================================================================

import bpy
from . import utils

def apply_undo_settings():
    prefs = bpy.context.preferences.edit
    addon_prefs = bpy.context.preferences.addons["bigbrain"].preferences

    try:
        prefs.undo_steps = addon_prefs.undo_steps
        utils.log(f"undo_steps set to {addon_prefs.undo_steps}")
    except Exception as e:
        utils.log(f"Failed to set undo_steps: {e}")

    try:
        prefs.undo_memory_limit = addon_prefs.undo_memory_limit
        utils.log(f"undo_memory_limit set to {addon_prefs.undo_memory_limit}")
    except Exception as e:
        utils.log(f"Failed to set undo_memory_limit: {e}")

def register():
    utils.conflicts = utils.detect_conflicts()

def unregister():
    pass
