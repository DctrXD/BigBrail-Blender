# =============================================================================
# BigBrain — Preferences UI
# Multilanguage, conflict warnings, reset button & version check.
# =============================================================================

import bpy
from . import utils

TEXTS = {
    'EN': {
        'title': "BigBrain Settings",
        'undo_steps': "Undo Steps",
        'undo_memory': "Undo Memory Limit (MB)",
        'version_warn': "⚠️ Blender version <2.93 may not be supported",
        'conflict_warn': "⚠️ Conflicting addons detected:",
        'reset': "Reset to Default",
        'lang': "Language",
    },
    'PT': {
        'title': "Configurações BigBrain",
        'undo_steps': "Passos de Desfazer",
        'undo_memory': "Limite de Memória (MB)",
        'version_warn': "⚠️ Blender <2.93 pode não ser suportado",
        'conflict_warn': "⚠️ Add-ons conflitantes:",
        'reset': "Resetar Padrão",
        'lang': "Idioma",
    },
    'ES': {
        'title': "Ajustes BigBrain",
        'undo_steps': "Pasos de Deshacer",
        'undo_memory': "Límite de Memoria (MB)",
        'version_warn': "⚠️ Blender <2.93 puede no ser compatible",
        'conflict_warn': "⚠️ Add-ons en conflicto:",
        'reset': "Restablecer Predeterminado",
        'lang': "Idioma",
    },
}

class BigBrainPreferences(bpy.types.AddonPreferences):
    bl_idname = "bigbrain"

    undo_steps: bpy.props.IntProperty(
        name="Undo Steps", default=512, min=32, max=10000
    )
    undo_memory_limit: bpy.props.IntProperty(
        name="Undo Memory Limit (MB)", default=0, min=0
    )
    language: bpy.props.EnumProperty(
        name="Language",
        items=[('EN','English',''),('PT','Português',''),('ES','Español','')],
        default='EN'
    )

    def draw(self, context):
        t = TEXTS[self.language]
        layout = self.layout

        # Title
        layout.label(text=t['title'], icon='RECOVER_AUTO')

        # Blender version check
        if bpy.app.version < (2, 93, 0):
            layout.label(text=t['version_warn'], icon='ERROR')

        # Language selector
        layout.prop(self, "language", text=t['lang'])

        # Undo settings
        layout.prop(self, "undo_steps", text=t['undo_steps'])
        layout.prop(self, "undo_memory_limit", text=t['undo_memory'])

        # Conflict warnings
        if utils.conflicts:
            layout.label(text=t['conflict_warn'], icon='ERROR')
            for c in utils.conflicts:
                layout.label(text=f"• {c}")

        # Reset button + hint
        layout.operator("bigbrain.reset_defaults", text=t['reset'], icon='LOOP_BACK')
        layout.label(text="Ctrl+Shift+R")
