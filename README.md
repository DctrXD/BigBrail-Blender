# 🧠 BigBrain v1.1.2 — Blender Addon  
> Infinite undo + live RAM + log viewer + i18n + conflicts + reset

![Blender](https://img.shields.io/badge/Blender-2.93%2B-orange?logo=blender)
![Version](https://img.shields.io/badge/version-1.1.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Author](https://img.shields.io/badge/author-github@DctrXD-black)

## 🚀 What’s New in 1.1.2

- Fixed missing `resource` import by using `bpy.app.memory_statistics`  
- Live RAM status in the status bar (updates every 1 s)  
- Fully working **Log Viewer** in 3D View → Sidebar → BigBrain  
- Version check warns if Blender < 2.93  
- Conflict detection lists other addons that tweak undo prefs  
- Reset-to-Default button + Ctrl + Shift + R keymap  

---

## 🧩 Features

- Custom undo steps (32–10000)  
- Configurable memory limit (0 = unlimited)  
- Live RAM usage in status bar  
- UI in English, Português or Español  
- Automatic detection of conflicting addons  
- One-click reset + shortcut  
- In-Blender log viewer with clear button  

---

## 🎯 Compatibility

🟢 **Blender 2.93+** (tested on 3.x & 4.x)  
⚠️ Older versions may not support all features.

---

## 📦 Installation

1. Clone or download this repo.  
2. From project root:
   ```bash
   zip -r bigbrain.zip bigbrain
   ```
3. In Blender:  
   `Edit > Preferences > Add-ons > Install...` → selecione `bigbrain.zip`  
4. Ative **BigBrain** e configure em Preferences → Add-ons.

---

## 🗒️ CHANGELOG

Confira [CHANGELOG.md](CHANGELOG.md).
