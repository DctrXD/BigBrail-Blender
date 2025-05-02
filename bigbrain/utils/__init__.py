# =============================================================================
# utils/__init__.py — Main utilities for BigBrain
# =============================================================================

import bpy
from . import logging
from . import ram_monitor
from . import conflicts
from . import diagnostics
from . import system

# Global variables
addon_keymaps = []

def register():
    """Register all utility modules"""
    logging.register()
    ram_monitor.register()
    conflicts.register()
    diagnostics.register()
    system.register()
    
    # Register keyboard shortcuts
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Reset defaults shortcut (Ctrl+Shift+R)
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("bigbrain.reset_defaults", 'R', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))
        
        # Toggle overlay shortcut (Ctrl+Shift+O)
        kmi = km.keymap_items.new("bigbrain.toggle_overlay", 'O', 'PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))
        
        # Show log viewer shortcut (Ctrl+Shift+L)
        kmi = km.keymap_items.new("wm.call_panel", 'L', 'PRESS', ctrl=True, shift=True)
        kmi.properties.name = "BIGBRAIN_PT_log_viewer"
        addon_keymaps.append((km, kmi))
    
    logging.log("BigBrain utilities registered")

def unregister():
    """Unregister all utility modules"""
    # Remove keyboard shortcuts
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    # Unregister modules in reverse order
    system.unregister()
    diagnostics.unregister()
    conflicts.unregister()
    ram_monitor.unregister()
    logging.unregister()
    
    logging.log("BigBrain utilities unregistered")

# Convenience functions to access from other modules
def log(message, level='INFO'):
    """Log a message with the specified level"""
    return logging.log(message, level)

def get_ram_usage():
    """Get current RAM usage in MB"""
    return ram_monitor.get_ram_usage()

def detect_conflicts():
    """Detect conflicting addons"""
    return conflicts.detect_conflicts()

def get_system_info():
    """Get system information"""
    return diagnostics.get_system_info()

def restart_blender():
    """Restart Blender"""
    return system.restart_blender()