# =============================================================================
# operators/toggle_overlay.py — Toggle RAM overlay in status bar
# =============================================================================

import bpy
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_OT_ToggleOverlay(bpy.types.Operator):
    bl_idname = "bigbrain.toggle_overlay"
    bl_label = "Toggle RAM Overlay"
    bl_description = "Toggle RAM usage display in the status bar"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        prefs.show_overlay = not prefs.show_overlay
        
        # Start or stop the RAM status display
        if prefs.show_overlay:
            utils.start_ram_status()
            utils.log(_('overlay_enabled'))
        else:
            utils.stop_ram_status()
            utils.log(_('overlay_disabled'))
            # Clear status bar
            context.window_manager.status_text_set(text="")
            
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ToggleOverlay)

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_OT_ToggleOverlay)