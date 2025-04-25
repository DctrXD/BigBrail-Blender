# =============================================================================
# Infinite Undo - User Preferences UI
# Author: github@DctrXD
# Summary: Creates a panel in Blender preferences to edit undo behavior.
# =============================================================================

import bpy

class InfiniteUndoPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # Number of undo steps (higher = deeper history)
    # Número de passos de desfazer (quanto maior, mais histórico)
    undo_steps: bpy.props.IntProperty(
        name="Undo Steps",
        description="Total undo levels (Ctrl+Z steps)",
        default=512,
        min=32,
        max=10000
    )

    # Memory limit for undo in MB (0 = unlimited)
    # Limite de memória para desfazer em MB (0 = ilimitado)
    undo_memory_limit: bpy.props.IntProperty(
        name="Undo Memory Limit (MB)",
        description="Max memory usage for undo system",
        default=0,
        min=0
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Infinite Undo Settings", icon='RECOVER_AUTO')
        layout.prop(self, "undo_steps")
        layout.prop(self, "undo_memory_limit")

def register():
    bpy.utils.register_class(InfiniteUndoPreferences)

def unregister():
    bpy.utils.unregister_class(InfiniteUndoPreferences)
