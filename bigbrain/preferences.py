# =============================================================================
# BigBrain — Preferences UI
# Provides settings panel in Blender Preferences > Add-ons
# =============================================================================

import bpy

class BigBrainPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    undo_steps: bpy.props.IntProperty(
        name="Undo Steps",
        description="How many Ctrl+Z steps (min 32, max 10000)",
        default=512, min=32, max=10000
    )
    undo_memory_limit: bpy.props.IntProperty(
        name="Undo Memory Limit (MB)",
        description="Max RAM for undo system (0 = unlimited)",
        default=0, min=0
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="BigBrain Undo Settings", icon='RECOVER_AUTO')
        layout.prop(self, "undo_steps")
        layout.prop(self, "undo_memory_limit")
        # Show Blender version
        version = bpy.app.version_string
        layout.label(text=f"Blender {version} detected")

def register():
    bpy.utils.register_class(BigBrainPreferences)

def unregister():
    bpy.utils.unregister_class(BigBrainPreferences)
