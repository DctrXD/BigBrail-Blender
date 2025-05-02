# =============================================================================
# utils/ram_monitor.py — RAM monitoring and overlay
# =============================================================================

import bpy
import time
import threading
import psutil
from ..i18n import get_text as _

# RAM history for graph
ram_history = []
vram_history = []
last_update_time = 0
MAX_HISTORY_POINTS = 100

# Timer for status updates
_timer = None

# Critical warning state
_critical_warning_shown = False
_last_warning_time = 0

def get_ram_usage():
    """Get current RAM usage in MB"""
    stats = bpy.app.memory_statistics()
    return stats.get("mem_in_use", 0) / (1024 * 1024)

def get_vram_usage():
    """Get current VRAM usage in MB if available"""
    stats = bpy.app.memory_statistics()
    
    # Blender 4.0+ changed the key for GPU memory
    if bpy.app.version >= (4, 0, 0):
        vram = stats.get("gpu_memory_in_use", 0)
    else:
        vram = stats.get("gpu_mem_in_use", 0)
        
    if vram > 0:
        return vram / (1024 * 1024)
    return 0

def get_system_ram():
    """Get system RAM info using psutil"""
    try:
        import psutil
        mem = psutil.virtual_memory()
        return {
            'total': mem.total / (1024 * 1024),  # Total RAM in MB
            'available': mem.available / (1024 * 1024),  # Available RAM in MB
            'used': mem.used / (1024 * 1024),  # Used RAM in MB
            'percent': mem.percent  # Percentage used
        }
    except ImportError:
        return {
            'total': 0,
            'available': 0,
            'used': 0,
            'percent': 0
        }

def get_fps():
    """Get current FPS"""
    return bpy.context.scene.render.fps / bpy.context.scene.render.fps_base

def format_ram(ram_mb):
    """Format RAM value for display"""
    if ram_mb > 1024:
        return f"{ram_mb/1024:.2f} GB"
    else:
        return f"{ram_mb:.0f} MB"

def update_status_text():
    """Update status bar text with RAM usage"""
    try:
        # Get preferences
        prefs = bpy.context.preferences.addons["bigbrain"].preferences
        
        # Skip if overlay is disabled
        if not prefs.show_overlay:
            return 1.0
        
        # Get RAM usage
        ram = get_ram_usage()
        
        # Format text based on preferences
        if prefs.compact_overlay:
            text = f"RAM: {format_ram(ram)}"
            
            # Add FPS if enabled
            if prefs.show_fps:
                fps = get_fps()
                text = f"FPS: {fps:.1f} | {text}"
            
            # Add VRAM if enabled and available
            if prefs.show_vram:
                vram = get_vram_usage()
                if vram > 0:
                    text = f"{text} | VRAM: {format_ram(vram)}"
        else:
            text = f"BigBrain | RAM Usage: {format_ram(ram)}"
            
            # Add system RAM if available
            sys_ram = get_system_ram()
            if sys_ram['total'] > 0:
                text = f"{text} | System: {sys_ram['percent']}% used"
            
            # Add FPS if enabled
            if prefs.show_fps:
                fps = get_fps()
                text = f"{text} | FPS: {fps:.1f}"
            
            # Add VRAM if enabled and available
            if prefs.show_vram:
                vram = get_vram_usage()
                if vram > 0:
                    text = f"{text} | VRAM: {format_ram(vram)}"
        
        # Set status text
        bpy.context.window_manager.status_text_set(text=text)
        
        # Check for critical RAM usage
        check_critical_ram(ram, prefs)
        
        # Return delay for next update
        return prefs.status_delay
    
    except Exception as e:
        print(f"[BigBrain] Error updating status: {e}")
        return 1.0

def check_critical_ram(ram, prefs):
    """Check if RAM usage is critical and show warning if needed"""
    global _critical_warning_shown, _last_warning_time
    
    # Skip if threshold is disabled
    if prefs.critical_threshold <= 0:
        return
    
    # Check if RAM usage exceeds threshold
    if ram > prefs.critical_threshold:
        # Only show warning once every 30 seconds
        current_time = time.time()
        if not _critical_warning_shown or (current_time - _last_warning_time > 30):
            _critical_warning_shown = True
            _last_warning_time = current_time
            
            # Show warning
            message = f"RAM usage is critical: {format_ram(ram)} > {format_ram(prefs.critical_threshold)}"
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            
            # Play sound if enabled
            if prefs.warning_sound:
                if hasattr(bpy.ops.sound, 'play_ui'):  # Blender 4.0+
                    bpy.ops.sound.play_ui(sound_type='ERROR')
                else:  # Older Blender versions
                    bpy.ops.sound.play_sound('INVOKE_DEFAULT')
            
            # Log warning
            from .. import utils
            utils.log(message, 'WARNING')
    else:
        _critical_warning_shown = False

def start_ram_status():
    """Start RAM status updates"""
    global _timer
    
    # Stop existing timer if running
    stop_ram_status()
    
    # Start new timer
    _timer = bpy.app.timers.register(
        update_status_text,
        first_interval=0.1,
        persistent=True
    )

def stop_ram_status():
    """Stop RAM status updates"""
    global _timer
    
    # Unregister timer if running
    if _timer and _timer in bpy.app.timers.timers():
        bpy.app.timers.unregister(_timer)
    
    _timer = None
    
    # Clear status text
    try:
        bpy.context.window_manager.status_text_set(text="")
    except:
        pass

def register():
    # Start RAM status if enabled in preferences
    try:
        prefs = bpy.context.preferences.addons["bigbrain"].preferences
        if prefs.show_overlay:
            start_ram_status()
    except:
        # Addon might not be fully registered yet
        pass

def unregister():
    stop_ram_status()