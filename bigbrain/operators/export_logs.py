# =============================================================================
# operators/export_logs.py — Export logs to a text file
# =============================================================================

import bpy
import os
import datetime
from .. import utils
from ..i18n import get_text as _

class BIGBRAIN_OT_ExportLogs(bpy.types.Operator):
    bl_idname = "bigbrain.export_logs"
    bl_label = "Export Logs"
    bl_description = "Export BigBrain logs to a text file"
    bl_options = {'REGISTER'}
    
    filepath: bpy.props.StringProperty(
        name="File Path",
        description="Path to save the log file",
        default="//bigbrain_logs.txt",
        subtype='FILE_PATH'
    )
    
    def invoke(self, context, event):
        # Set default filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filepath = f"//bigbrain_logs_{timestamp}.txt"
        
        # Show file browser
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    
    def execute(self, context):
        # Resolve the filepath (handle // for relative paths)
        filepath = bpy.path.abspath(self.filepath)
        
        try:
            # Create directory if it doesn't exist
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Write logs to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"BigBrain Logs - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                for entry in utils.log_entries:
                    f.write(f"{entry}\n")
            
            # Log the action
            utils.log(_('logs_exported').format(filepath))
            self.report({'INFO'}, _('logs_exported').format(filepath))
            
            return {'FINISHED'}
            
        except Exception as e:
            utils.log(f"Error exporting logs: {e}")
            self.report({'ERROR'}, f"Error exporting logs: {e}")
            return {'CANCELLED'}

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ExportLogs)

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_OT_ExportLogs)