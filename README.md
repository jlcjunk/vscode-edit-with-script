# Edit with Script

**Run any shell command on selected text** — instantly.

- **50 customizable scripts**  
- **Keyboard shortcuts**
- **Command Palette** ( `Ctrl+Shift+P` → `Edit with Script: Script` )  
- **Right-click menu**

---

## Features

| Feature                       | Description                                             |
|-------------------------------|---------------------------------------------------------|
| **No temp files**             | Streams input/output directly                           |
| **Uses your terminal shell**  | Respects `terminal.integrated.shell.*`                  |
| **User-safe config**          | Scripts in Settings, keybindings in `keybindings.json`  |
| **Cross-platform**            | Linux, macOS, Windows                                   |

---

## Installation

### Option 1: Install from VSIX (Recommended)

1. **Download** the latest `.vsix` from [Releases](https://github.com/jlcjunk/vscode-edit-with-script/releases)
2. In VS Code:
   - Press `Ctrl+Shift+P`
   - Type: `Extensions: Install from VSIX…`
   - Select the `.vsix` file
3. **Reload** VS Code

### Option 2: Build from Source

```bash
git clone https://github.com/jlcjunk/vscode-edit-with-script.git
cd vscode-edit-with-script
code --install-extension edit-with-script-*.vsix


---

## Configuration

### 1. Configure Scripts

1. Press `Ctrl + ,`  
2. Search: `Edit with Script`  
3. Edit any of the 50 fields:

| Setting     | Example                                                    |
|-------------|------------------------------------------------------------|
| `Script 01` | `date`                                                     |
| `Script 06` | `sed 's/\t/ /g'`                                           |
| `Script 10` | `python3 -c "import sys; print(sys.stdin.read().upper())"` |

> **Your settings are preserved on update**

---

### 2. Configure Keyboard Shortcuts

Edit your **user keybindings**:

**File → Preferences → Keyboard Shortcuts (JSON)**  
or press `Ctrl+Shift+P` → `Preferences: Open Keyboard Shortcuts (JSON)`

```json
[
  { "key": "ctrl+alt+1",   "command": "editWithScript.run01", "when": "editorTextFocus" },
  { "key": "ctrl+alt+2",   "command": "editWithScript.run02", "when": "editorTextFocus" },
  { "key": "ctrl+alt+3",   "command": "editWithScript.run03", "when": "editorTextFocus" },
  { "key": "ctrl+alt+4",   "command": "editWithScript.run04", "when": "editorTextFocus" },
  { "key": "ctrl+alt+5",   "command": "editWithScript.run05", "when": "editorTextFocus" },
  { "key": "ctrl+alt+6",   "command": "editWithScript.run06", "when": "editorTextFocus" },
  { "key": "ctrl+alt+7",   "command": "editWithScript.run07", "when": "editorTextFocus" },
  { "key": "ctrl+alt+8",   "command": "editWithScript.run08", "when": "editorTextFocus" },
  { "key": "ctrl+alt+9",   "command": "editWithScript.run09", "when": "editorTextFocus" },
  { "key": "ctrl+alt+0",   "command": "editWithScript.run10", "when": "editorTextFocus" },

  { "key": "ctrl+alt+f1",  "command": "editWithScript.run11", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f2",  "command": "editWithScript.run12", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f3",  "command": "editWithScript.run13", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f4",  "command": "editWithScript.run14", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f5",  "command": "editWithScript.run15", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f6",  "command": "editWithScript.run16", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f7",  "command": "editWithScript.run17", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f8",  "command": "editWithScript.run18", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f9",  "command": "editWithScript.run19", "when": "editorTextFocus" },
  { "key": "ctrl+alt+f10", "command": "editWithScript.run20", "when": "editorTextFocus" }
]


