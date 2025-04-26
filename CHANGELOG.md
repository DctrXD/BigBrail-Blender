# Changelog

## [1.1.2] – 2025-04-27
### Fixed
- Removed `resource` import; now uses `bpy.app.memory_statistics`
- Eliminated console errors on Windows
- Ensured all classes register/unregister cleanly

### Added
- Log viewer panel (3D View → Sidebar → BigBrain)
- Clear logs operator
- All log messages captured and viewable
- RAM status in status bar via timer callback

## [1.1.1] – 2025-04-27
- Hotfix: fixed operators, i18n, status bar timer

## [1.1.0] – 2025-04-26
- RAM graph, i18n, conflict detection, reset button, version check

## [1.0.1] – 2025-04-25
- API mismatch fix, error handling

## [1.0.0] – 2025-04-24
- Initial release
