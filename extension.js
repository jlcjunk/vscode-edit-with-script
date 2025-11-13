'use strict';
const vscode = require('vscode');
const cp = require('child_process');
const os = require('os');

function getShell() {
  const config = vscode.workspace.getConfiguration('terminal.integrated');
  const platform = os.platform();
  if (platform === 'win32') return config.get('shell.windows') || 'cmd.exe';
  if (platform === 'darwin') return config.get('shell.osx') || '/bin/zsh';
  return config.get('shell.linux') || '/bin/bash';
}

function runScript(cmd) {
  const editor = vscode.window.activeTextEditor;
  if (!editor) return;
  const selection = editor.selection;
  const input = editor.document.getText(selection);
  const shell = getShell();
  const shellArgs = os.platform() === 'win32' ? ['/d', '/c'] : ['-c'];

  const proc = cp.spawn(shell, [...shellArgs, cmd], { stdio: ['pipe', 'pipe', 'pipe'] });
  let stdout = '', stderr = '';
  proc.stdout.on('data', d => stdout += d);
  proc.stderr.on('data', d => stderr += d);
  proc.on('close', code => {
    if (code !== 0) {
      vscode.window.showErrorMessage(`Script failed: ${stderr.trim() || cmd}`);
      return;
    }
    editor.edit(edit => edit.replace(selection, stdout));
  });
  proc.stdin.end(input);
}

function activate(context) {
  for (let i = 1; i <= 50; i++) {
    const num = i.toString().padStart(2, '0');
    const cmdId = `editWithScript.run${num}`;
    context.subscriptions.push(vscode.commands.registerCommand(cmdId, () => {
      const cfg = vscode.workspace.getConfiguration('editWithScript');
      const script = cfg.get(`cmd${num}`, '').trim();
      if (!script) {
        vscode.window.showWarningMessage(`Script ${num} is empty`);
        return;
      }
      runScript(script);
    }));
  }
}

exports.activate = activate;
