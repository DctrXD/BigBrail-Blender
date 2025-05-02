# =============================================================================
# ui/terminal_panel.py — Mini terminal panel for command execution
# =============================================================================

import bpy
import re
import sys
import traceback
from .. import utils
from ..i18n import get_text as _

# Store command history
command_history = []
history_index = -1
terminal_output = []
MAX_HISTORY = 20
MAX_OUTPUT_LINES = 15

class BIGBRAIN_OT_ExecuteCommand(bpy.types.Operator):
    bl_idname = "bigbrain.execute_command"
    bl_label = "Execute Command"
    bl_description = "Execute Python command in BigBrain mini terminal"
    
    command: bpy.props.StringProperty(
        name="Command",
        description="Python command to execute"
    )
    
    def execute(self, context):
        global command_history, history_index, terminal_output
        
        if not self.command.strip():
            return {'CANCELLED'}
        
        # Add to history if not a duplicate of the last command
        if not command_history or command_history[-1] != self.command:
            command_history.append(self.command)
            if len(command_history) > MAX_HISTORY:
                command_history.pop(0)
        
        # Reset history index
        history_index = -1
        
        # Log the command
        utils.log(f"Terminal: {self.command}")
        terminal_output.append(f">>> {self.command}")
        
        # Execute the command
        try:
            # Create a local namespace with access to bpy
            namespace = {
                'bpy': bpy,
                'C': bpy.context,
                'D': bpy.data,
                'utils': utils
            }
            
            # Execute the command
            result = eval(self.command, namespace)
            
            # Add result to output
            if result is not None:
                terminal_output.append(str(result))
                
        except SyntaxError:
            # If it's not a simple expression, try exec
            try:
                exec(self.command, namespace)
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                terminal_output.append(error_msg)
                utils.log(error_msg)
                
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            terminal_output.append(error_msg)
            utils.log(error_msg)
        
        # Limit output lines
        if len(terminal_output) > MAX_OUTPUT_LINES:
            terminal_output = terminal_output[-MAX_OUTPUT_LINES:]
        
        # Clear the command field
        context.scene.bigbrain_terminal_command = ""
        
        return {'FINISHED'}

class BIGBRAIN_OT_ClearTerminal(bpy.types.Operator):
    bl_idname = "bigbrain.clear_terminal"
    bl_label = "Clear Terminal"
    bl_description = "Clear the terminal output"
    
    def execute(self, context):
        global terminal_output
        terminal_output.clear()
        utils.log("Terminal cleared")
        return {'FINISHED'}

class BIGBRAIN_OT_HistoryCommand(bpy.types.Operator):
    bl_idname = "bigbrain.history_command"
    bl_label = "History Command"
    bl_description = "Navigate command history"
    
    direction: bpy.props.EnumProperty(
        items=[
            ('UP', "Up", "Previous command"),
            ('DOWN', "Down", "Next command")
        ],
        name="Direction"
    )
    
    def execute(self, context):
        global history_index
        
        if not command_history:
            return {'CANCELLED'}
        
        if self.direction == 'UP':
            # Go back in history
            if history_index < len(command_history) - 1:
                history_index += 1
        else:  # DOWN
            # Go forward in history
            if history_index > -1:
                history_index -= 1
        
        # Set the command
        if history_index >= 0:
            context.scene.bigbrain_terminal_command = command_history[-(history_index+1)]
        else:
            context.scene.bigbrain_terminal_command = ""
        
        return {'FINISHED'}

class BIGBRAIN_PT_Terminal(bpy.types.Panel):
    bl_label = "BigBrain Terminal"
    bl_idname = "BIGBRAIN_PT_terminal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BigBrain'
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        # Only show if terminal is enabled in preferences
        prefs = context.preferences.addons["bigbrain"].preferences
        return hasattr(prefs, "show_terminal") and prefs.show_terminal
    
    def draw(self, context):
        layout = self.layout
        
        # Output area
        box = layout.box()
        col = box.column(align=True)
        
        if not terminal_output:
            col.label(text=_('terminal_empty'))
        else:
            for line in terminal_output:
                # Wrap long lines
                if len(line) > 40:
                    wrapped_lines = [line[i:i+40] for i in range(0, len(line), 40)]
                    for wrapped in wrapped_lines:
                        col.label(text=wrapped)
                else:
                    col.label(text=line)
        
        # Command input
        row = layout.row(align=True)
        row.prop(context.scene, "bigbrain_terminal_command", text="")
        
        # History navigation buttons
        sub = row.row(align=True)
        sub.scale_x = 0.5
        sub.operator("bigbrain.history_command", text="▲").direction = 'UP'
        sub.operator("bigbrain.history_command", text="▼").direction = 'DOWN'
        
        # Execute and clear buttons
        row = layout.row(align=True)
        row.operator("bigbrain.execute_command", text=_('terminal_execute'), icon='CONSOLE')
        row.operator("bigbrain.clear_terminal", text="", icon='X')

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ExecuteCommand)
    bpy.utils.register_class(BIGBRAIN_OT_ClearTerminal)
    bpy.utils.register_class(BIGBRAIN_OT_HistoryCommand)
    bpy.utils.register_class(BIGBRAIN_PT_Terminal)
    
    # Register the command property
    bpy.types.Scene.bigbrain_terminal_command = bpy.props.StringProperty(
        name="Command",
        description="Python command to execute"
    )

def unregister():
    bpy.utils.unregister_class(BIGBRAIN_PT_Terminal)
    bpy.utils.unregister_class(BIGBRAIN_OT_HistoryCommand)
    bpy.utils.unregister_class(BIGBRAIN_OT_ClearTerminal)
    bpy.utils.unregister_class(BIGBRAIN_OT_ExecuteCommand)
    
    # Unregister the command property
    if hasattr(bpy.types.Scene, "bigbrain_terminal_command"):
        del bpy.types.Scene.bigbrain_terminal_command