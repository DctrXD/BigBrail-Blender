# =============================================================================
# config.py — Applies undo prefs & detects conflicts
# =============================================================================

import bpy
from . import utils
from .i18n import get_text as _

def apply_undo_settings():
    """Apply undo settings from addon preferences to Blender preferences"""
    prefs = bpy.context.preferences.edit
    addon_prefs = bpy.context.preferences.addons["bigbrain"].preferences

    try:
        # Set undo steps
        prefs.undo_steps = addon_prefs.undo_steps
        utils.log(_('undo_steps_set').format(addon_prefs.undo_steps))
    except Exception as e:
        utils.log(f"Failed to set undo_steps: {e}", 'ERROR')

    try:
        # Set undo memory limit
        prefs.undo_memory_limit = addon_prefs.undo_memory_limit
        utils.log(_('undo_memory_set').format(addon_prefs.undo_memory_limit))
    except Exception as e:
        utils.log(f"Failed to set undo_memory_limit: {e}", 'ERROR')
    
    # Start RAM status if enabled
    if addon_prefs.show_overlay:
        utils.ram_monitor.start_ram_status()
    else:
        utils.ram_monitor.stop_ram_status()

def check_for_updates():
    """Check for addon updates"""
    return utils.system.check_for_updates()

def register():
    """Register config module"""
    # Detect conflicts on startup
    utils.conflicts = utils.conflicts.detect_conflicts()
    
    # Log configuration
    utils.log("Configuration module registered")

def unregister():
    """Unregister config module"""
    pass
