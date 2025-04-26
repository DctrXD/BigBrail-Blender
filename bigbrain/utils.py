# =============================================================================
# BigBrain — Utilities: Conflict Detection & Reset Operator + Keymap
# =============================================================================

import bpy

# will be populated at startup
conflicts: list[str] = []

def detect_conflicts() -> list[str]:
    """🇬🇧 Find other addons that adjust undo settings. 🇧🇷 Detecta addons conflitantes."""
    conflicts_list = []
    prefs = bpy.context.preferences
    for name, addon in prefs.addons.items():
        if name == __package__: continue
        ap = addon.preferences
        if hasattr(ap, 'undo_steps') or hasattr(ap, 'undo_memory_limit'):
            conflicts_list.append(name)
    return conflicts_list

# Reset Operator
class BIGBRAIN_OT_ResetDefaults(bpy.types.Operator):
    bl_idname = "bigbrain.reset_defaults"
    bl_label = "Reset BigBrain Settings"
    bl_description = "🇬🇧 Reset settings to defaults. 🇧🇷 Reseta para valores padrão."

    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences
        from .preferences import BigBrainPreferences
        # restore defaults from bl_rna
        props = BigBrainPreferences.bl_rna.properties
        prefs.undo_steps        = props['undo_steps'].default
        prefs.undo_memory_limit = props['undo_memory_limit'].default
        prefs.language          = props['language'].default
        return {'FINISHED'}

# keymap storage
addon_keymaps = []

def register():
    bpy.utils.register_class(BIGBRAIN_OT_ResetDefaults)
    # add Ctrl+Shift+R in Window context
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new("bigbrain.reset_defaults", type='R', value='PRESS', ctrl=True, shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # remove keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(BIGBRAIN_OT_ResetDefaults)
