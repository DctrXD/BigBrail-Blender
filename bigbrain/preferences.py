# =============================================================================
# BigBrain — Preferences UI with RAM Graph, Multi-Lang & Reset Button
# =============================================================================

import bpy
from . import utils

# Texts for multilanguage
TEXTS = {
    'EN': {
        'settings': "BigBrain Undo Settings",
        'undo_steps': "Undo Steps",
        'undo_memory': "Memory Limit (MB)",
        'ram_usage': "RAM Usage: {used:.1f} / {total:.1f} MB",
        'conflict_warning': "⚠️ Conflict with other addons detected:",
        'reset_button': "Reset to Default",
        'reset_shortcut': "Shortcut: Ctrl+Shift+R",
        'language': "Language",
    },
    'PT': {
        'settings': "Configurações do BigBrain",
        'undo_steps': "Passos de Desfazer",
        'undo_memory': "Limite de Memória (MB)",
        'ram_usage': "Uso de RAM: {used:.1f} / {total:.1f} MB",
        'conflict_warning': "⚠️ Conflito detectado com outros addons:",
        'reset_button': "Resetar Padrão",
        'reset_shortcut': "Atalho: Ctrl+Shift+R",
        'language': "Idioma",
    },
    'ES': {
        'settings': "Ajustes de BigBrain",
        'undo_steps': "Pasos de Deshacer",
        'undo_memory': "Límite de Memoria (MB)",
        'ram_usage': "Uso de RAM: {used:.1f} / {total:.1f} MB",
        'conflict_warning': "⚠️ Conflicto detectado con otros addons:",
        'reset_button': "Restablecer Predeterminado",
        'reset_shortcut': "Atajo: Ctrl+Shift+R",
        'language': "Idioma",
    },
}

class BigBrainPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # Basic settings
    undo_steps: bpy.props.IntProperty(
        name="Undo Steps", default=512, min=32, max=10000
    )
    undo_memory_limit: bpy.props.IntProperty(
        name="Undo Memory Limit (MB)", default=0, min=0
    )
    # Multilanguage selector
    language: bpy.props.EnumProperty(
        name="Language",
        items=[
            ('EN','English',''),
            ('PT','Português',''),
            ('ES','Español',''),
        ],
        default='EN'
    )
    # Memory gauge (0.0–1.0)
    memory_percent: bpy.props.FloatProperty(
        name="RAM Usage %", default=0.0, min=0.0, max=1.0
    )

    def draw(self, context):
        t = TEXTS[self.language]
        layout = self.layout

        # Section title
        layout.label(text=t['settings'], icon='RECOVER_AUTO')
        # Language choice
        layout.prop(self, "language", text=t['language'])

        # Undo settings
        layout.prop(self, "undo_steps", text=t['undo_steps'])
        layout.prop(self, "undo_memory_limit", text=t['undo_memory'])

        # Real-time RAM usage
        stats = bpy.app.memory_statistics()
        used = stats.get('mem_in_use', 0) / (1024*1024)
        total = stats.get('mem_limit', 1) / (1024*1024)
        self.memory_percent = min(1.0, used / total)
        layout.label(text=t['ram_usage'].format(used=used, total=total))
        layout.template_progress_bar(self, "memory_percent")

        # Conflict warnings
        if utils.conflicts:
            layout.label(text=t['conflict_warning'], icon='ERROR')
            for c in utils.conflicts:
                layout.label(text=f"• {c}")

        # Reset button + shortcut hint
        layout.separator()
        layout.operator("bigbrain.reset_defaults", text=t['reset_button'], icon='LOOP_BACK')
        layout.label(text=t['reset_shortcut'])

def register():
    bpy.utils.register_class(BigBrainPreferences)

def unregister():
    bpy.utils.unregister_class(BigBrainPreferences)
