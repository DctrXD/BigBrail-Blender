# =============================================================================
# ui/header_status.py — Header display for RAM usage
# =============================================================================

import bpy
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_HT_Header(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    
    def draw(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        
        # Only draw if overlay is enabled
        if not prefs.show_overlay:
            return
        
        layout = self.layout
        
        # Create a separate row to push content to the right
        row = layout.row()
        row.alignment = 'RIGHT'
        
        # BigBrain label
        row.label(text="BB", icon='MEMORY')
        
        # RAM usage
        stats = bpy.app.memory_statistics()
        used_ram = stats.get("mem_in_use", 0) / (1024 * 1024)  # Convert to MB
        
        # Format based on size
        if used_ram > 1024:
            ram_text = f"{used_ram/1024:.2f} GB"
        else:
            ram_text = f"{used_ram:.1f} MB"
        
        # Color based on threshold
        if hasattr(prefs, "critical_threshold") and prefs.critical_threshold > 0:
            if used_ram > prefs.critical_threshold:
                row.alert = True
        
        row.label(text=ram_text)
        
        # FPS if enabled
        if hasattr(prefs, "show_fps") and prefs.show_fps:
            fps = context.scene.render.fps / context.scene.render.fps_base
            row.label(text=f"{fps:.1f} FPS")
        
        # VRAM if enabled and available
        if hasattr(prefs, "show_vram") and prefs.show_vram:
            vram = stats.get("gpu_mem_in_use", 0)
            if vram > 0:
                vram_mb = vram / (1024 * 1024)
                if vram_mb > 1024:
                    vram_text = f"{vram_mb/1024:.2f} GB"
                else:
                    vram_text = f"{vram_mb:.1f} MB"
                row.label(text=f"VRAM: {vram_text}")
        
        # Toggle button
        row.operator("bigbrain.toggle_overlay", text="", icon='HIDE_OFF')

def register():
    bpy.utils.register_class(BIGBRAIN_HT_Header)

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_HT_Header)