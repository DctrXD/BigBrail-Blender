# =============================================================================
# operators/reset_defaults.py — Reset preferences to default values
# =============================================================================

import bpy
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_OT_ResetDefaults(bpy.types.Operator):
    bl_idname = "bigbrain.reset_defaults"
    bl_label = "Reset BigBrain Settings"
    bl_description = "Reset all BigBrain settings to their default values"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        
        # Reset all properties to their default values
        for prop in [
            "undo_steps", 
            "undo_memory_limit", 
            "status_delay", 
            "show_overlay", 
            "language",
            "critical_threshold",
            "warning_sound",
            "show_graph",
            "graph_width",
            "graph_height",
            "compact_overlay",
            "show_fps",
            "show_vram",
            "log_to_file",
            "log_level",
            "auto_disable_conflicts"
        ]:
            if hasattr(prefs, prop):
                try:
                    default = type(prefs).bl_rna.properties[prop].default
                    setattr(prefs, prop, default)
                except Exception as e:
                    utils.log(f"Failed to reset {prop}: {e}")
        
        # Log the action
        utils.log(_('settings_reset'))
        self.report({"INFO"}, _('settings_reset_notification'))
        
        # Apply the new undo settings
        from .. import config
        config.apply_undo_settings()
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ResetDefaults)

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_OT_ResetDefaults)