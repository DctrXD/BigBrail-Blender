# =============================================================================
# preferences.py — UI: undo prefs, i18n, version warning, conflicts, reset, overlay & delay
# =============================================================================

import bpy
from . import utils

TEXTS = {
    'EN': {
        'title': "BigBrain Settings",
        'undo_steps': "Undo Steps",
        'undo_memory': "Undo Memory Limit (MB)",
        'delay': "Status Delay (s)",
        'overlay': "Show RAM Overlay",
        'version_warn': "⚠️ Blender <2.93 may not be supported",
        'conflict_warn': "⚠️ Conflicting addons detected:",
        'reset': "Reset to Default",
        'lang': "Language",
    },
    'PT': {
        'title': "Configurações BigBrain",
        'undo_steps': "Passos de Desfazer",
        'undo_memory': "Limite de Memória (MB)",
        'delay': "Atraso do Status (s)",
        'overlay': "Mostrar Sobreposição de RAM",
        'version_warn': "⚠️ Blender <2.93 pode não ser suportado",
        'conflict_warn': "⚠️ Add-ons conflitantes:",
        'reset': "Resetar Padrão",
        'lang': "Idioma",
    },
    'ES': {
        'title': "Ajustes BigBrain",
        'undo_steps': "Pasos de Deshacer",
        'undo_memory': "Límite de Memoria (MB)",
        'delay': "Retraso de Estado (s)",
        'overlay': "Mostrar Superposición de RAM",
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
    status_delay: bpy.props.FloatProperty(
        name="Status Delay (s)", default=1.0, min=0.1
    )
    show_overlay: bpy.props.BoolProperty(
        name="Show RAM Overlay", default=False
    )
    language: bpy.props.EnumProperty(
        name="Language",
        items=[('EN','English',''),('PT','Português',''),('ES','Español','')],
        default='EN'
    )

    def draw(self, context):
        t = TEXTS[self.language]
        layout = self.layout

        layout.label(text=t['title'], icon='RECOVER_AUTO')

        if bpy.app.version < (2,93,0):
            layout.label(text=t['version_warn'], icon='ERROR')

        layout.prop(self, "language", text=t['lang'])
        layout.prop(self, "undo_steps", text=t['undo_steps'])
        layout.prop(self, "undo_memory_limit", text=t['undo_memory'])
        layout.prop(self, "status_delay", text=t['delay'])
        layout.prop(self, "show_overlay", text=t['overlay'])

        if utils.conflicts:
            layout.label(text=t['conflict_warn'], icon='ERROR')
            for c in utils.conflicts:
                layout.label(text=f"• {c}")

        layout.operator("bigbrain.reset_defaults", text=t['reset'], icon='LOOP_BACK')
        layout.label(text="Ctrl+Shift+R")
