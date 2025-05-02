# 🧠 BigBrain v2.0.0 — Advanced Memory Management for Blender

A comprehensive memory management and diagnostics addon for Blender. Tested on Blender 2.93+ with special optimizations for 3.x and 4.x.

![Blender](https://img.shields.io/badge/Blender-2.93%2B-orange?logo=blender)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Author](https://img.shields.io/badge/author-github@DctrXD-black)

## 🚀 What's New in 2.0.0

- 🔄 Full Blender 4.0+ compatibility
- 📊 RAM usage graph with customizable dimensions
- 🖥️ VRAM monitoring (when available)
- ⚠️ Critical RAM usage warnings with sound alerts
- 📋 Enhanced Log Viewer with export functionality
- 🔍 System diagnostics and driver checks
- 🛠️ Conflict detection and resolution
- 🌐 Expanded i18n support (English, Português, Español)
- 🔄 Auto-update checking

---

## 🧩 Features

- **Memory Management**
  - Custom undo steps (32–10000)
  - Configurable undo memory limit (MB)
  - Live RAM monitoring in status bar & header
  - Optional RAM graph overlay
  - VRAM usage monitoring
  - Critical RAM threshold warnings

- **User Interface**
  - "BB" indicator in 3D View header
  - Toggle overlay button in header
  - Compact/detailed display modes
  - Customizable update frequency
  - FPS display option

- **Diagnostics & Logging**
  - Comprehensive system information
  - GPU driver status check
  - Conflict detection with other addons
  - Log viewer with filtering
  - Log export functionality
  - Python terminal in sidebar

- **Internationalization**
  - English, Português, and Español support
  - Easily extensible translation system

- **Utilities**
  - One-click reset (Ctrl+Shift+R)
  - Auto-update checking
  - Blender 4.0+ compatibility mode

---

## 🎯 Compatibility

🟢 **Blender 2.93+** (fully tested on 3.x & 4.x)  
✅ Special optimizations for Blender 4.0+  
⚠️ Older versions might lack some features

---

## 📦 Installation

```bash
git clone https://github.com/DctrXD/BigBrain.git
cd BigBrain
zip -r bigbrain.zip bigbrain
```

In Blender:  
`Edit > Preferences > Add-ons > Install…` → select `bigbrain.zip` → Activate the addon

---

## 🛠️ Usage

1. **Memory Monitoring**: RAM usage is displayed in the status bar automatically
2. **Header Controls**: Click "BB" in the 3D View header to toggle the overlay
3. **Preferences**: Configure in Edit > Preferences > Add-ons > BigBrain
4. **Log Viewer**: Access in the 3D View sidebar under the "BigBrain" tab
5. **Diagnostics**: Run system checks via the "Diagnose" button in preferences
6. **Reset**: Use the reset button or press Ctrl+Shift+R to restore defaults

---

## 🗒️ CHANGELOG

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.
