# =============================================================================
# ui/__init__.py — BigBrain UI package
# =============================================================================

from . import (
    log_viewer,
    header_status,
    overlay_draw,
    terminal_panel
)

def register():
    log_viewer.register()
    header_status.register()
    overlay_draw.register()
    terminal_panel.register()

def unregister():
    terminal_panel.unregister()
    overlay_draw.unregister()
    header_status.unregister()
    log_viewer.unregister()