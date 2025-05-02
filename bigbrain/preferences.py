# =============================================================================
# Preferences UI: undo settings, i18n, version warning, conflict list, reset button
# =============================================================================

import bpy
import os
from . import utils, version
from .i18n import get_text as _

class BigBrainPreferences(bpy.types.AddonPreferences):
    bl_idname = "bigbrain"

    # Undo settings
    undo_steps: bpy.props.IntProperty(
        name="Undo Steps", 
        description="Number of undo steps to keep in memory",
        default=512, 
        min=32, 
        max=10000
    )
    
    undo_memory_limit: bpy.props.IntProperty(
        name="Undo Memory Limit (MB)", 
        description="Maximum memory to use for undo (0 = unlimited)",
        default=0, 
        min=0
    )
    
    # Display settings
    status_delay: bpy.props.FloatProperty(
        name="Status Delay (s)", 
        description="Delay between status updates in seconds",
        default=1.0, 
        min=0.1
    )
    
    show_overlay: bpy.props.BoolProperty(
        name="Show RAM Overlay", 
        description="Show RAM usage in the status bar",
        default=True
    )
    
    show_graph: bpy.props.BoolProperty(
        name="Show RAM Graph", 
        description="Show RAM usage graph overlay",
        default=False
    )
    
    graph_width: bpy.props.IntProperty(
        name="Graph Width", 
        description="Width of the RAM graph in pixels",
        default=200, 
        min=100, 
        max=500
    )
    
    graph_height: bpy.props.IntProperty(
        name="Graph Height", 
        description="Height of the RAM graph in pixels",
        default=100, 
        min=50, 
        max=300
    )
    
    compact_overlay: bpy.props.BoolProperty(
        name="Compact Overlay", 
        description="Use compact display for RAM overlay",
        default=False
    )
    
    show_fps: bpy.props.BoolProperty(
        name="Show FPS", 
        description="Show FPS in the overlay",
        default=False
    )
    
    show_vram: bpy.props.BoolProperty(
        name="Show VRAM", 
        description="Show VRAM usage in the overlay if available",
        default=True
    )
    
    # Warning settings
    critical_threshold: bpy.props.IntProperty(
        name="Critical RAM Threshold (MB)", 
        description="Show warning when RAM usage exceeds this value (0 = disabled)",
        default=0, 
        min=0
    )
    
    warning_sound: bpy.props.BoolProperty(
        name="Play Warning Sound", 
        description="Play sound when RAM usage exceeds critical threshold",
        default=False
    )
    
    warning_sound_file: bpy.props.StringProperty(
        name="Warning Sound File", 
        description="Sound file to play when RAM usage exceeds critical threshold",
        default="",
        subtype='FILE_PATH'
    )
    
    # Logging settings
    log_to_file: bpy.props.BoolProperty(
        name="Log to File", 
        description="Save logs to file",
        default=False
    )
    
    log_location: bpy.props.StringProperty(
        name="Log Location", 
        description="Directory to save log files",
        default="",
        subtype='DIR_PATH'
    )
    
    log_level: bpy.props.EnumProperty(
        name="Log Level",
        description="Minimum log level to record",
        items=[
            ('DEBUG', "Debug", "Show all log messages including debug"),
            ('INFO', "Info", "Show info, warning and error messages"),
            ('WARNING', "Warning", "Show only warning and error messages"),
            ('ERROR', "Error", "Show only error messages")
        ],
        default='INFO'
    )
    
    # Terminal settings
    show_terminal: bpy.props.BoolProperty(
        name="Show Terminal", 
        description="Show Python terminal in sidebar",
        default=False
    )
    
    # Conflict settings
    auto_disable_conflicts: bpy.props.BoolProperty(
        name="Auto-disable Conflicts", 
        description="Automatically disable conflicting addons",
        default=False
    )
    
    # Language settings
    language: bpy.props.EnumProperty(
        name="Language",
        description="Interface language",
        items=[
            ('EN', 'English', ''),
            ('PT', 'Português', ''),
            ('ES', 'Español', '')
        ],
        default='EN'
    )
    
    # Blender 4.0+ compatibility settings
    use_blender4_compat: bpy.props.BoolProperty(
        name="Blender 4.0+ Compatibility", 
        description="Enable special compatibility mode for Blender 4.0+",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        
        # Main settings
        layout.label(text=_('title'), icon='RECOVER_AUTO')
        
        # Version info
        version_status = version.get_update_status()
        box = layout.box()
        row = box.row()
        row.label(text=f"BigBrain v{version.VERSION_STRING}", icon='INFO')
        
        # Update status
        if version_status['update_available']:
            row = box.row()
            row.label(text=f"Update available: v{version_status['latest_version']}", icon='ERROR')
            row.operator("bigbrain.open_update_page", text="Get Update", icon='URL')
        
        row = box.row()
        row.operator("bigbrain.check_for_updates", text="Check for Updates", icon='FILE_REFRESH')
        
        # Blender version warning
        if bpy.app.version < (2, 93, 0):
            box.label(text=_('version_warn'), icon='ERROR')
        elif bpy.app.version >= (4, 0, 0):
            box.label(text=f"Running on Blender {bpy.app.version_string} (4.0+ compatibility mode)", icon='INFO')
            box.prop(self, "use_blender4_compat")
        
        # Create tabs
        tab_box = layout.box()
        row = tab_box.row()
        row.prop(self, "language", text=_('lang'))
        
        # Main settings
        box = layout.box()
        box.label(text=_('undo_settings'), icon='LOOP_BACK')
        
        col = box.column(align=True)
        col.prop(self, "undo_steps", text=_('undo_steps'))
        col.prop(self, "undo_memory_limit", text=_('undo_memory'))
        
        # Display settings
        box = layout.box()
        box.label(text=_('display_settings'), icon='SCREEN_BACK')
        
        col = box.column(align=True)
        row = col.row()
        row.prop(self, "show_overlay", text=_('show_overlay'))
        row.prop(self, "compact_overlay", text=_('compact_overlay'))
        
        col.prop(self, "status_delay", text=_('status_delay'))
        
        # Graph settings
        sub_box = box.box()
        sub_box.enabled = self.show_overlay
        row = sub_box.row()
        row.prop(self, "show_graph", text=_('show_graph'))
        
        if self.show_graph:
            col = sub_box.column(align=True)
            col.prop(self, "graph_width", text=_('graph_width'))
            col.prop(self, "graph_height", text=_('graph_height'))
        
        # Additional display options
        col = box.column(align=True)
        col.enabled = self.show_overlay
        col.prop(self, "show_fps", text=_('show_fps'))
        col.prop(self, "show_vram", text=_('show_vram'))
        
        # Warning settings
        box = layout.box()
        box.label(text=_('warning_settings'), icon='ERROR')
        
        col = box.column(align=True)
        col.prop(self, "critical_threshold", text=_('critical_threshold'))
        
        row = col.row()
        row.enabled = self.critical_threshold > 0
        row.prop(self, "warning_sound", text=_('warning_sound'))
        
        if self.warning_sound and self.critical_threshold > 0:
            col.prop(self, "warning_sound_file", text="")
        
        # Logging settings
        box = layout.box()
        box.label(text=_('logging_settings'), icon='TEXT')
        
        col = box.column(align=True)
        col.prop(self, "log_level", text=_('log_level'))
        col.prop(self, "log_to_file", text=_('log_to_file'))
        
        if self.log_to_file:
            col.prop(self, "log_location", text=_('log_location'))
        
        # Terminal settings
        box = layout.box()
        box.prop(self, "show_terminal", text=_('show_terminal'))
        
        # Conflict settings
        box = layout.box()
        box.label(text=_('conflict_settings'), icon='CANCEL')
        
        col = box.column()
        col.prop(self, "auto_disable_conflicts", text=_('auto_disable_conflicts'))
        
        # Show detected conflicts
        if utils.conflicts:
            col.label(text=_('conflict_warn'), icon='ERROR')
            for conflict in utils.conflicts:
                col.label(text=f"• {conflict}")
        
        # Action buttons
        row = layout.row()
        row.operator("bigbrain.reset_defaults", text=_('reset'), icon='LOOP_BACK')
        row.operator("bigbrain.diagnose_conflicts", text=_('diagnose'), icon='VIEWZOOM')
        row.operator("bigbrain.export_logs", text=_('export_logs'), icon='EXPORT')

def register():
    bpy.utils.register_class(BigBrainPreferences)
    utils.log("Preferences registered")

def unregister():
    bpy.utils.unregister_class(BigBrainPreferences)