# =============================================================================
# operators/__init__.py — BigBrain operators package
# =============================================================================

from . import (
    reset_defaults,
    toggle_overlay,
    export_logs,
    diagnose_conflicts
)

# Importar operadores do módulo version
from ..version import (
    BIGBRAIN_OT_CheckForUpdates,
    BIGBRAIN_OT_OpenUpdatePage
)

def register():
    reset_defaults.register()
    toggle_overlay.register()
    export_logs.register()
    diagnose_conflicts.register()
    # Os operadores de version são registrados no próprio módulo version

def unregister():
    diagnose_conflicts.unregister()
    export_logs.unregister()
    toggle_overlay.unregister()
    reset_defaults.unregister()
    # Os operadores de version são desregistrados no próprio módulo version