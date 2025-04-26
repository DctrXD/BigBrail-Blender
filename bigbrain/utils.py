# =============================================================================
# BigBrain — Utilities: conflict detection, reset operator & RAM status.
# =============================================================================

import bpy
import resource  # Unix-only; on Windows this will fail, so we catch it.

conflicts = []
_timer = None

def detect_conflicts():
    prefs = bpy.context.preferences.addons
    found = []
    for name, mod in prefs.items():
        if name == "bigbrain": continue
        ap = mod.preferences
        if hasattr(ap, "undo_steps") or hasattr(ap, "undo_memory_limit"):
            found.append(name)
    return found

class BIGBRAIN_OT_ResetDefaults(bpy.types.Operator):
    bl_idname = "bigbrain.reset_defaults"
    bl_label = "BigBrain Reset"

    def execute(self, context):
        prefs = context.preferences.addons["bigbrain"].preferences
        props = BigBrainPreferences.bl_rna.properties
        prefs.undo_steps        = props['undo_steps'].default
        prefs.undo_memory_limit = props['undo_memory_limit'].default
        prefs.language          = props['language'].default
        self.report({'INFO'}, "BigBrain settings reset")
        return {'FINISHED'}

def _ram_status_callback():
    used = 0.0
    try:
        used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
    except Exception:
        pass
    wm = bpy.context.window_manager
    wm.status_text_set(f"BigBrain RAM: {used:.1f} MB")
    return 1.0  # repeat every second

def start_ram_status():
    global _timer
    if _timer is None:
        _timer = bpy.app.timers.register(_ram_status_callback, first_interval=1.0)

def stop_ram_status():
    global _timer
    if _timer is not None:
        bpy.app.timers.unregister(_ram_status_callback)
        _timer = None

addon_keymaps = []

def register():
    from .preferences import BigBrainPreferences
    bpy.utils.register_class(BIGBRAIN_OT_ResetDefaults)
    # keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("bigbrain.reset_defaults",
                                  type='R', value='PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(BIGBRAIN_OT_ResetDefaults)
