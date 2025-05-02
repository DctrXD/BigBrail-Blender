# =============================================================================
# operators/diagnose_conflicts.py — Diagnose and resolve addon conflicts
# =============================================================================

import bpy
import sys
import platform
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_OT_DiagnoseConflicts(bpy.types.Operator):
    bl_idname = "bigbrain.diagnose_conflicts"
    bl_label = "Diagnose Conflicts"
    bl_description = "Run diagnostics to find and resolve conflicts with other addons"
    bl_options = {'REGISTER'}
    
    auto_disable: bpy.props.BoolProperty(
        name="Auto-disable Conflicts",
        description="Automatically disable conflicting addons",
        default=False
    )
    
    def invoke(self, context, event):
        # Show confirmation dialog
        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "auto_disable")
        
        # Show current conflicts
        if utils.conflicts:
            layout.label(text=_('conflict_warn'), icon='ERROR')
            for conflict in utils.conflicts:
                layout.label(text=f"• {conflict}")
    
    def execute(self, context):
        # Detect conflicts
        conflicts = utils.detect_conflicts()
        
        # System info for diagnostics
        system_info = {
            "os": platform.platform(),
            "python": sys.version,
            "blender": bpy.app.version_string,
            "gpu": bpy.context.preferences.system.compute_device_type
        }
        
        # Log system info
        utils.log(f"Diagnostic run - System info:")
        for key, value in system_info.items():
            utils.log(f"  {key}: {value}")
        
        # Log conflicts
        if conflicts:
            utils.log(f"Found {len(conflicts)} conflicting addon(s):")
            for addon in conflicts:
                utils.log(f"  • {addon}")
                
            # Auto-disable if requested
            if self.auto_disable:
                for addon in conflicts:
                    try:
                        bpy.ops.preferences.addon_disable(module=addon)
                        utils.log(f"Disabled conflicting addon: {addon}")
                    except Exception as e:
                        utils.log(f"Failed to disable {addon}: {e}")
                
                # Update conflicts list
                utils.conflicts = utils.detect_conflicts()
                
                self.report({'INFO'}, _('conflicts_disabled').format(len(conflicts)))
            else:
                self.report({'WARNING'}, _('conflicts_found').format(len(conflicts)))
        else:
            utils.log("No conflicts detected")
            self.report({'INFO'}, _('no_conflicts'))
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(BIGBRAIN_OT_DiagnoseConflicts)

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_OT_DiagnoseConflicts)