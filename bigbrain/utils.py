# =============================================================================
# utils.py — logging, conflict detection, reset op, log viewer, header draw & RAM status
# =============================================================================

import bpy

conflicts = []
log_entries = []
_timer = None
addon_keymaps = []

def log(msg):
    log_entries.append(msg)

def detect_conflicts():
    found = []
    for name, mod in bpy.context.preferences.addons.items():
        if name != "bigbrain" and hasattr(mod.preferences, "undo_steps"):
            found.append(name)
    log(f"Conflicts: {found}")
    return found

class BIGBRAIN_OT_ResetDefaults(bpy.types.Operator):
    bl_idname = "bigbrain.reset_defaults"
    bl_label = "BigBrain Reset"

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        for prop in ["undo_steps","undo_memory_limit","status_delay","show_overlay","language"]:
            default = type(prefs).bl_rna.properties[prop].default
            setattr(prefs, prop, default)
        log("Settings reset to default")
        self.report({"INFO"},"BigBrain settings reset")
        return {"FINISHED"}

class BIGBRAIN_OT_ClearLogs(bpy.types.Operator):
    bl_idname = "bigbrain.clear_logs"
    bl_label = "Clear Logs"

    def execute(self, context):
        log_entries.clear()
        self.report({"INFO"},"Logs cleared")
        return {"FINISHED"}

class BIGBRAIN_PT_LogViewer(bpy.types.Panel):
    bl_label = "BigBrain Logs"
    bl_idname = "BIGBRAIN_PT_log_viewer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'BigBrain'

    def draw(self, context):
        layout = self.layout
        for entry in log_entries[-20:]:
            layout.label(text=entry)
        layout.operator("bigbrain.clear_logs", icon='X')

class BIGBRAIN_HT_Header(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    def draw(self, context):
        layout = self.layout
        layout.label(text="BB")
        # live RAM
        stats = bpy.app.memory_statistics()
        used = stats.get("mem_in_use",0)/(1024*1024)
        layout.label(text=f"{used:.1f}MB")
        # overlay toggle button
        layout.operator("bigbrain.toggle_overlay", text="", icon='HIDE_OFF')

class BIGBRAIN_OT_ToggleOverlay(bpy.types.Operator):
    bl_idname = "bigbrain.toggle_overlay"
    bl_label = "Toggle RAM Overlay"

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        prefs.show_overlay = not prefs.show_overlay
        log(f"Overlay {'on' if prefs.show_overlay else 'off'}")
        return {"FINISHED"}

def _ram_status_callback():
    prefs = bpy.context.preferences.addons["bigbrain"].preferences
    stats = bpy.app.memory_statistics()
    used = stats.get("mem_in_use",0)/(1024*1024)
    # status bar
    bpy.context.window_manager.status_text_set(f"BigBrain RAM: {used:.1f} MB")
    return prefs.status_delay

def start_ram_status():
    global _timer
    if _timer is None:
        _timer = bpy.app.timers.register(_ram_status_callback, first_interval=1.0)

def stop_ram_status():
    global _timer
    if _timer is not None:
        bpy.app.timers.unregister(_ram_status_callback)
        _timer = None

def register():
    for cls in (
        BIGBRAIN_OT_ResetDefaults,
        BIGBRAIN_OT_ClearLogs,
        BIGBRAIN_PT_LogViewer,
        BIGBRAIN_HT_Header,
        BIGBRAIN_OT_ToggleOverlay,
    ):
        bpy.utils.register_class(cls)
    # keymap for reset
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("bigbrain.reset_defaults", 'R','PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km,kmi))
    log("Utils registered")

def unregister():
    stop_ram_status()
    for km,kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    for cls in reversed([
        BIGBRAIN_OT_ToggleOverlay,
        BIGBRAIN_HT_Header,
        BIGBRAIN_PT_LogViewer,
        BIGBRAIN_OT_ClearLogs,
        BIGBRAIN_OT_ResetDefaults,
    ]):
        bpy.utils.unregister_class(cls)
    log("Utils unregistered")
