# =============================================================================
# utils/conflicts.py — Detect and manage conflicting addons
# =============================================================================

import bpy
from ..i18n import get_text as _

# List of known conflicting addons
conflicts = []

# List of addon features that might conflict
CONFLICT_FEATURES = [
    "undo_steps",           # Addons that modify undo steps
    "undo_memory_limit",    # Addons that modify undo memory limit
    "memory_statistics",    # Addons that display memory statistics
    "performance_monitor",  # Addons that monitor performance
]

def detect_conflicts():
    """
    Detect addons that might conflict with BigBrain
    
    Returns:
        List of conflicting addon names
    """
    global conflicts
    found = []
    
    # Check all enabled addons
    for name, mod in bpy.context.preferences.addons.items():
        # Skip BigBrain itself
        if name == "bigbrain":
            continue
        
        # Check if addon has preferences
        if not hasattr(mod, "preferences") or mod.preferences is None:
            continue
        
        # Check for conflicting features
        for feature in CONFLICT_FEATURES:
            if hasattr(mod.preferences, feature):
                found.append(name)
                break
        
        # Check for specific known conflicts
        if name in ["performance_monitor", "memory_stats", "undo_manager"]:
            found.append(name)
    
    # Update global conflicts list
    conflicts = found
    
    # Log the conflicts
    from .. import utils
    if found:
        utils.log(f"Detected {len(found)} conflicting addon(s): {', '.join(found)}", 'WARNING')
    else:
        utils.log("No conflicting addons detected", 'INFO')
    
    return found

def disable_conflicts():
    """
    Disable all conflicting addons
    
    Returns:
        List of disabled addon names
    """
    disabled = []
    
    # Get current conflicts
    conflicts = detect_conflicts()
    
    # Disable each conflicting addon
    for addon in conflicts:
        try:
            bpy.ops.preferences.addon_disable(module=addon)
            disabled.append(addon)
            from .. import utils
            utils.log(f"Disabled conflicting addon: {addon}", 'INFO')
        except Exception as e:
            from .. import utils
            utils.log(f"Failed to disable {addon}: {e}", 'ERROR')
    
    # Update conflicts list
    detect_conflicts()
    
    return disabled

def get_conflict_details():
    """
    Get detailed information about conflicts
    
    Returns:
        Dictionary with conflict details
    """
    details = {}
    
    for name in conflicts:
        try:
            mod = bpy.context.preferences.addons.get(name)
            if not mod:
                continue
            
            # Get addon info
            bl_info = getattr(mod.module, "bl_info", {})
            
            details[name] = {
                "name": bl_info.get("name", name),
                "version": ".".join(str(v) for v in bl_info.get("version", (0, 0, 0))),
                "author": bl_info.get("author", "Unknown"),
                "description": bl_info.get("description", ""),
                "conflict_reason": "Modifies undo settings or monitors performance"
            }
        except:
            details[name] = {
                "name": name,
                "version": "Unknown",
                "author": "Unknown",
                "description": "",
                "conflict_reason": "Unknown conflict"
            }
    
    return details

def register():
    """Register conflict detection"""
    # Detect conflicts on startup
    detect_conflicts()

def unregister():
    """Unregister conflict detection"""
    global conflicts
    conflicts = []