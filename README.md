# Edit with Script

Run **20 shell scripts** on selected text using:
- **Keyboard shortcuts** (`Ctrl+Alt+1` → `Ctrl+Alt+0`, `Ctrl+Alt+F1` → `F10`)
- **Right-click menu**
- **Command Palette**

---

## Installation



1. Clone repository to local systems
  git clone https://github.com/jlcjunk/vscode-edit-with-script.git
  
2. Run VSCode

3. Install extension from vsix
  press CTRL+Shift+p
  search - vsix
  select- Extensions: Install from VSIX
  locate the cloned repo and select vsix file
  install
  reload VSCode

## configure Keyboard shortcuts
  press CTRL+Shift+p
  Select Preferences: Open Keyboard Shortcuts (JSON)
  Edit Keyboard shortcuts to your needs
  
### example:
// Place your key bindings in this file to override the defaults
// keybindings.json
[
  { "key": "ctrl+alt+1",  "command": "editWithScript.run01", "when": "editorTextFocus" },
  { "key": "ctrl+alt+2",  "command": "editWithScript.run02", "when": "editorTextFocus" },
  { "key": "ctrl+alt+3",  "command": "editWithScript.run03", "when": "editorTextFocus" },
  { "key": "ctrl+alt+4",  "command": "editWithScript.run04", "when": "editorTextFocus" },
  { "key": "ctrl+alt+5",  "command": "editWithScript.run05", "when": "editorTextFocus" },
  { "key": "ctrl+alt+6",  "command": "editWithScript.run06", "when": "editorTextFocus" },
  { "key": "ctrl+alt+7",  "command": "editWithScript.run07", "when": "editorTextFocus" },
  { "key": "ctrl+alt+8",  "command": "editWithScript.run08", "when": "editorTextFocus" },
  { "key": "ctrl+alt+9",  "command": "editWithScript.run09", "when": "editorTextFocus" },
  { "key": "ctrl+alt+0",  "command": "editWithScript.run10", "when": "editorTextFocus" },

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



##  Configure scripts
  Press Ctrl + ,
  Search: editwithscript
  Edit any Script 01 → Script 20





