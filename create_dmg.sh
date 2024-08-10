#!/bin/sh

# Remove any existing DMG file
test -f ClipLLM-Installer.dmg && rm ClipLLM-Installer.dmg

create-dmg \
  --volname "ClipLLM Installer" \
  --volicon "clipllm_icon.icns" \
  --background "installer_background.png" \
  --window-pos "200 120" \
  --window-size "800 400" \
  --icon-size "100" \
  --icon "ClipLLM.app" "200 190" \
  --hide-extension "ClipLLM.app" \
  --app-drop-link "600 185" \
  "ClipLLM-Installer.dmg" \
  "dist/"