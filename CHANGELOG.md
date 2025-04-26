# Changelog

## [1.1.1] – 2025-04-27
### Fixed
- Removed invalid `conflicts: list[str]` annotation to prevent console errors.
- Ensured all Python imports (`resource`) are caught to avoid crashes.
- Proper keymap registration/unregistration.
- Verified multilanguage, conflict detection, reset button all draw in UI.
- Implemented live RAM status via `bpy.app.timers` → status bar.

### Added
- None — bug-fix release.

## [1.1.0] – 2025-04-26
- Live RAM graph **in prefs** (replaced by status bar in 1.1.1).
- i18n (EN/PT/ES), conflict detection, reset button + keymap, version check.

## [1.0.1] – 2025-04-25
- API mismatch fix (`preferences.edit`), error handling, version badge.

## [1.0.0] – 2025-04-24
- Initial unlimited undo addon.
