# Changelog

## [1.0.1] – YYYY-MM-DD
### Fixed
- Use `preferences.edit` instead of `preferences.system` for undo API.
- Added `try/except` around settings write to prevent AttributeError.
- Display detected Blender version in UI.

### Updated
- README badges and version to 1.0.1.
- bl_info metadata.
- Tutorial & release instructions.

## [1.0.0] – initial release
- Unlimited undo steps & memory via Blender Preferences.
- Modular code: config, preferences, utils.