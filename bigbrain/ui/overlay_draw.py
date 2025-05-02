# =============================================================================
# ui/overlay_draw.py — Custom overlay drawing for RAM graph
# =============================================================================

import bpy
import gpu
import blf
import time
from gpu_extras.batch import batch_for_shader
from .. import utils
from ..i18n import get_text as _

# Store RAM history for graph
ram_history = []
last_update_time = 0
MAX_HISTORY_POINTS = 100

def get_ram_usage():
    """Get current RAM usage in MB"""
    stats = bpy.app.memory_statistics()
    return stats.get("mem_in_use", 0) / (1024 * 1024)

def update_ram_history():
    """Update RAM history for graph"""
    global ram_history, last_update_time
    
    # Limit update frequency
    current_time = time.time()
    if current_time - last_update_time < 0.5:  # Update every 0.5 seconds
        return
    
    last_update_time = current_time
    
    # Add current RAM usage to history
    ram_history.append(get_ram_usage())
    
    # Limit history size
    if len(ram_history) > MAX_HISTORY_POINTS:
        ram_history.pop(0)

def draw_ram_graph(context):
    """Draw RAM usage graph overlay"""
    prefs = context.preferences.addons["bigbrain"].preferences
    
    # Check if graph should be shown
    if not hasattr(prefs, "show_graph") or not prefs.show_graph:
        return
    
    # Update RAM history
    update_ram_history()
    
    # Get graph dimensions
    width = prefs.graph_width
    height = prefs.graph_height
    
    # Position in bottom right corner with padding
    region = context.region
    x = region.width - width - 20
    y = 20
    
    # Draw background
    draw_rect(x, y, width, height, (0.0, 0.0, 0.0, 0.5))
    
    # Draw graph if we have enough data
    if len(ram_history) > 1:
        # Find max value for scaling
        max_ram = max(ram_history)
        if max_ram <= 0:
            max_ram = 1  # Avoid division by zero
        
        # Draw graph lines
        draw_graph_lines(x, y, width, height, ram_history, max_ram)
        
        # Draw current value
        current_ram = ram_history[-1]
        blf.color(0, 1.0, 1.0, 1.0, 1.0)
        blf.position(0, x + 5, y + height - 20, 0)
        blf.size(0, 12)
        
        # Format RAM value
        if current_ram > 1024:
            ram_text = f"{current_ram/1024:.2f} GB"
        else:
            ram_text = f"{current_ram:.0f} MB"
        
        blf.draw(0, f"RAM: {ram_text}")
        
        # Draw max value
        blf.position(0, x + 5, y + 5, 0)
        if max_ram > 1024:
            max_text = f"Max: {max_ram/1024:.2f} GB"
        else:
            max_text = f"Max: {max_ram:.0f} MB"
        blf.draw(0, max_text)

def draw_rect(x, y, width, height, color):
    """Draw a rectangle with the given dimensions and color"""
    if bpy.app.version >= (4, 0, 0):
        # Blender 4.0+ shader approach
        with gpu.matrix.push_pop():
            # Set up the shader
            shader = gpu.shader.from_builtin('UNIFORM_COLOR')
            batch = batch_for_shader(
                shader, 'TRI_FAN',
                {
                    "pos": ((x, y), (x + width, y), (x + width, y + height), (x, y + height)),
                }
            )
            
            # Draw the rectangle
            shader.bind()
            shader.uniform_float("color", color)
            batch.draw(shader)
    else:
        # Blender 2.93-3.x approach
        vertices = ((x, y), (x + width, y), (x + width, y + height), (x, y + height))
        indices = ((0, 1, 2), (0, 2, 3))
        
        shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
        batch = batch_for_shader(shader, 'TRIS', {"pos": vertices}, indices=indices)
        
        shader.bind()
        shader.uniform_float("color", color)
        batch.draw(shader)

def draw_graph_lines(x, y, width, height, data, max_value):
    """Draw graph lines for the given data"""
    if not data or len(data) < 2:
        return
    
    # Calculate points
    points = []
    for i, value in enumerate(data):
        px = x + (i / (len(data) - 1)) * width
        py = y + (value / max_value) * height
        points.append((px, py))
    
    # Draw lines
    if bpy.app.version >= (4, 0, 0):
        # Blender 4.0+ shader approach
        with gpu.matrix.push_pop():
            shader = gpu.shader.from_builtin('UNIFORM_COLOR')
            batch = batch_for_shader(shader, 'LINE_STRIP', {"pos": points})
            
            shader.bind()
            shader.uniform_float("color", (0.0, 1.0, 0.0, 1.0))
            batch.draw(shader)
    else:
        # Blender 2.93-3.x approach
        shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')
        batch = batch_for_shader(shader, 'LINE_STRIP', {"pos": points})
        
        shader.bind()
        shader.uniform_float("color", (0.0, 1.0, 0.0, 1.0))
        batch.draw(shader)

# Drawing handler
_draw_handle = None

def register_draw_handler():
    """Register the drawing handler"""
    global _draw_handle
    if _draw_handle is None:
        _draw_handle = bpy.types.SpaceView3D.draw_handler_add(
            draw_ram_graph, (bpy.context,), 'WINDOW', 'POST_PIXEL')

def unregister_draw_handler():
    """Unregister the drawing handler"""
    global _draw_handle
    if _draw_handle is not None:
        bpy.types.SpaceView3D.draw_handler_remove(_draw_handle, 'WINDOW')
        _draw_handle = None

def register():
    register_draw_handler()

def unregister():
    unregister_draw_handler()