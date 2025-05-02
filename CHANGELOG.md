# Changelog

## [2.0.0] - 2023-11-15
### Added
- Full Blender 4.0+ compatibility with special optimizations
- RAM usage graph with customizable dimensions
- VRAM monitoring capabilities
- Critical RAM usage warnings with sound alerts
- System diagnostics and driver checks
- Auto-update checking functionality
- Expanded i18n support
- Log export functionality
- Python terminal in sidebar

### Improved
- Completely refactored codebase for better organization
- Enhanced conflict detection and resolution
- Optimized RAM monitoring for better performance
- Improved UI with more configuration options

## [1.2.3] - 2023-04-26
### Added
- "BB" label in View3D header  
- Live RAM & "Toggle Overlay" button in header  
- Configurable status delay (`status_delay`)  
- show_overlay toggle → header overlay  
- Log Viewer panel in Sidebar  
- Updated doc_url to github.com/DctrXD  

### Fixed
- resource import error removed; uses `memory_statistics`

## [1.1.2] - 2023-04-26
### Fixed
- Removed `resource` import; now uses `bpy.app.memory_statistics`
- Eliminated console errors on Windows
- Ensured all classes register/unregister cleanly

### Added
- Log viewer panel (3D View → Sidebar → BigBrain)
- Clear logs operator
- All log messages captured and viewable
- RAM status in status bar via timer callback

## [1.1.1] - 2023-04-26
- Hotfix: fixed operators, i18n, status bar timer

## [1.1.0] - 2023-04-26
- RAM graph, i18n, conflict detection, reset button, version check

## [1.0.1] - 2023-04-25
- API mismatch fix, error handling

## [1.0.0] - 2023-04-24
- Initial release
