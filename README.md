# 🧠 BigBrain v1.0.1 — Blender Addon  
> Maximize your Ctrl+Z. Undo like a genius.

![Blender](https://img.shields.io/badge/Blender-2.93%2B-orange?logo=blender)
![Version](https://img.shields.io/badge/version-1.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Author](https://img.shields.io/badge/author-github@DctrXD-black)

## 🚀 What’s New in 1.0.1

- ✅ **Fixed** API mismatch: now uses `preferences.edit.undo_steps` & `undo_memory_limit`  
- ✅ **Version check** badge + runtime detection of Blender version  
- ✅ **Robust error handling**: logs any failures to set attributes  
- 🔧 Updated docs & CHANGELOG  

---

## 🧩 Features

- Custom undo steps (32–10000)  
- Configurable memory limit (MB) or unlimited  
- Persists across sessions  
- Ready for future backup/timeline tools  

---

## 🎯 Compatibility

🟢 **Blender 2.93+** (fully tested on 3.x & 4.x)  
⚠️ May not work on older releases.

---

## 📦 Installation

1. Clone or download this repo.  
2. From project root:
   ```bash
   zip -r bigbrain.zip bigbrain
   ```
3. In Blender:  
   `Edit > Preferences > Add-ons > Install...` → selecione `bigbrain.zip`  
4. Ative o **BigBrain** e ajuste as preferências.

---

## ⛓️ GitHub Release

See [CHANGELOG.md](CHANGELOG.md) for details.

---

## 🧑‍💻 Author

github@DctrXD | MIT License  
Built with ☕ & Ctrl+Z frustrations.