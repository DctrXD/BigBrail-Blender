# =============================================================================
# ui/log_viewer.py — Log viewer panel and filter controls
# =============================================================================

import bpy
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_OT_ClearLogs(bpy.types.Operator):
    bl_idname = "bigbrain.clear_logs"
    bl_label = "Clear Logs"
    bl_description = "Clear all log entries"
    
    def execute(self, context):
        utils.log_entries.clear()
        utils.log(_('logs_cleared'))
        self.report({"INFO"}, _('logs_cleared'))
        return {"FINISHED"}

class BIGBRAIN_PT_LogViewer(bpy.types.Panel):
    bl_label = "BigBrain Logs"
    bl_idname = "BIGBRAIN_PT_log_viewer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BigBrain'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        # Filter controls
        row = layout.row(align=True)
        row.label(text=_('log_filter'))
        
        # Log level filter (if implemented)
        if hasattr(context.scene, "bigbrain_log_filter"):
            row.prop(context.scene, "bigbrain_log_filter", text="")
        
        # Log entries
        box = layout.box()
        col = box.column(align=True)
        
        if not utils.log_entries:
            col.label(text=_('no_logs'))
        else:
            # Show the most recent logs (limited to avoid performance issues)
            for entry in utils.log_entries[-20:]:
                # Determine icon based on log content (optional)
                icon = 'INFO'
                if "error" in entry.lower() or "failed" in entry.lower():
                    icon = 'ERROR'
                elif "warning" in entry.lower():
                    icon = 'ERROR'
                
                # Wrap long lines
                if len(entry) > 40:
                    wrapped_lines = [entry[i:i+40] for i in range(0, len(entry), 40)]
                    for i, wrapped in enumerate(wrapped_lines):
                        # Only show icon on first line
                        if i == 0:
                            col.label(text=wrapped, icon=icon)
                        else:
                            col.label(text=wrapped)
                else:
                    col.label(text=entry, icon=icon)
        
        # Action buttons
        row = layout.row(align=True)
        row.operator("bigbrain.clear_logs", icon='X')
        row.operator("bigbrain.export_logs", icon='EXPORT')

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ClearLogs)
    bpy.utils.register_class(BIGBRAIN_PT_LogViewer)
    
    # Register log filter property
    bpy.types.Scene.bigbrain_log_filter = bpy.props.EnumProperty(
        name="Log Filter",
        items=[
            ('ALL', _('filter_all'), "Show all log entries"),
            ('INFO', _('filter_info'), "Show info entries only"),
            ('WARNING', _('filter_warning'), "Show warning entries only"),
            ('ERROR', _('filter_error'), "Show error entries only")
        ],
        default='ALL'
    )

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_PT_LogViewer)
    bpy.utils.unregister_class(BIGBRAIN_OT_ClearLogs)
    
    # Unregister log filter property
    if hasattr(bpy.types.Scene, "bigbrain_log_filter"):
        del bpy.types.Scene.bigbrain_log_filter