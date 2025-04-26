# =============================================================================
# Utilities: logging, conflict detection, reset operator, clear logs, log viewer, RAM status
# =============================================================================

import bpy

conflicts = []
log_entries = []
_timer = None
addon_keymaps = []

def log(message):
    log_entries.append(message)

def detect_conflicts():
    found = []
    for name, mod in bpy.context.preferences.addons.items():
        if name != "bigbrain" and hasattr(mod.preferences, "undo_steps"):
            found.append(name)
    log(f"Conflict detection found: {found}")
    return found

class BIGBRAIN_OT_ResetDefaults(bpy.types.Operator):
    bl_idname = "bigbrain.reset_defaults"
    bl_label = "Reset Default Settings"

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        props = type(prefs).bl_rna.properties
        prefs.undo_steps = props["undo_steps"].default
        prefs.undo_memory_limit = props["undo_memory_limit"].default
        prefs.language = props["language"].default
        log("Settings reset to default")
        self.report({"INFO"}, "BigBrain settings reset")
        return {"FINISHED"}

class BIGBRAIN_OT_ClearLogs(bpy.types.Operator):
    bl_idname = "bigbrain.clear_logs"
    bl_label = "Clear Logs"

    def execute(self, context):
        log_entries.clear()
        self.report({"INFO"}, "BigBrain logs cleared")
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
        layout.operator("bigbrain.clear_logs")

def _ram_status_callback():
    stats = bpy.app.memory_statistics()
    used = stats.get("mem_in_use", 0) / (1024*1024)
    bpy.context.window_manager.status_text_set(f"BigBrain RAM: {used:.1f} MB")
    return 1.0

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
    bpy.utils.register_class(BIGBRAIN_OT_ResetDefaults)
    bpy.utils.register_class(BIGBRAIN_OT_ClearLogs)
    bpy.utils.register_class(BIGBRAIN_PT_LogViewer)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "bigbrain.reset_defaults", type='R', value='PRESS', ctrl=True, shift=True
        )
        addon_keymaps.append((km, kmi))
    log("Utils registered")

def unregister():
    stop_ram_status()
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(BIGBRAIN_PT_LogViewer)
    bpy.utils.unregister_class(BIGBRAIN_OT_ClearLogs)
    bpy.utils.unregister_class(BIGBRAIN_OT_ResetDefaults)
    log("Utils unregistered")
