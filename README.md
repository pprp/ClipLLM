# ClipLLM

Clipboard as a Bridge to AI Communication

ClipLLM is a project that explores using the clipboard as an interface for AI communication.

## Features

- Read and write data to the clipboard
- Communicate with AI models using clipboard data
- Easy-to-use Python interface

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pprp/ClipLLM.git
   cd ClipLLM
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:

```bash
python src/main.py
```

For detailed usage instructions, refer to the [documentation](docs/usage.md).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

ClipLLM is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on GitHub.

<!-- ## How to get dmg file

```
pip install pyinstaller
```

create ClipLLM.spec

```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['interface.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ClipLLM',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ClipLLM')

app = BUNDLE(coll,
             name='ClipLLM.app',
             icon=None,
             bundle_identifier=None)
```

run pyinstaller with this spec file:

```
pyinstaller ClipLLM.spec
```

You may need to adjust permissions for the app to access the clipboard and keyboard input. You can do this by adding the necessary entitlements to your app. Create a file called entitlements.plist:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.device.audio-input</key>
    <true/>
    <key>com.apple.security.device.camera</key>
    <true/>
    <key>com.apple.security.personal-information.addressbook</key>
    <true/>
    <key>com.apple.security.personal-information.calendars</key>
    <true/>
</dict>
</plist>
```

5. Sign your application with these entitlements:

```
codesign --entitlements entitlements.plist -s - dist/ClipLLM.app
```

```
pip install py2app
```

create setup.py

```
from setuptools import setup

APP = ['interface.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5'],
    'plist': {
        'CFBundleName': 'ClipLLM',
        'CFBundleDisplayName': 'ClipLLM',
        'CFBundleGetInfoString': "Making ClipLLM",
        'CFBundleIdentifier': "com.yourcompany.ClipLLM",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, Your Company, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

Run py2app in alias mode first to test:

```
python setup.py py2app -A
```

create standalone application:

```
python setup.py py2app
```

Your application should now be in dist/ClipLLM.app. 6. To create a DMG, you can use the create-dmg command as described in the previous response:

```

I apologize for the inconvenience. If create-dmg isn't working, there are alternative methods to create a DMG file. Let's try using the built-in macOS tools to create a DMG. Here's a step-by-step process:


First, create a new directory for your DMG contents:


mkdir ClipLLM-dmg


Copy your application into this new directory:


cp -R dist/ClipLLM.app ClipLLM-dmg/


Now, use the hdiutil command to create the DMG:

hdiutil create -volname "ClipLLM Installer" -srcfolder ClipLLM-dmg -ov -format UDZO ClipLLM.dmg

```

<!-- iconutil -c iconset brain.icns -->

hdiutil detach /Volumes/ClipLLM\ Installer
hdiutil convert ClipLLM.dmg -format UDRW -o ClipLLM_rw.dmg
hdiutil attach ClipLLM_rw.dmg
cp brain.iconset/icon_512x512.png /Volumes/ClipLLM\ Installer/.VolumeIcon.icns
SetFile -a C /Volumes/ClipLLM\ Installer
touch /Volumes/ClipLLM\ Installer

hdiutil detach /Volumes/ClipLLM\ Installer
hdiutil convert ClipLLM_rw.dmg -format UDZO -o ClipLLM_final.dmg
rm ClipLLM_rw.dmg -->

## How to get dmg file

To create a DMG file for ClipLLM, follow these steps:

1. Install required tools:

```bash
pip install pyinstaller py2app
```

2. Create a `setup.py` file in your project directory:

```python
from setuptools import setup

APP = ['interface.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5'],
    'plist': {
        'CFBundleName': 'ClipLLM',
        'CFBundleDisplayName': 'ClipLLM',
        'CFBundleGetInfoString': "Making ClipLLM",
        'CFBundleIdentifier': "com.yourcompany.ClipLLM",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, Your Company, All Rights Reserved"
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

3. Build the application:

```bash
python setup.py py2app
```

4. Create a folder for the DMG contents:

```bash
mkdir ClipLLM-dmg
cp -R dist/ClipLLM.app ClipLLM-dmg/
ln -s /Applications ClipLLM-dmg/
```

5. Create the initial DMG:

```bash
hdiutil create -volname "ClipLLM Installer" -srcfolder ClipLLM-dmg -ov -format UDZO ClipLLM.dmg
```

6. To add a custom icon to the DMG:

```bash
# Convert icon to iconset if not already done
iconutil -c iconset brain.icns

# Convert DMG to read-write format
hdiutil convert ClipLLM.dmg -format UDRW -o ClipLLM_rw.dmg

# Mount the read-write DMG
hdiutil attach ClipLLM_rw.dmg

# Copy the icon and set attributes
cp brain.iconset/icon_512x512.png /Volumes/ClipLLM\ Installer/.VolumeIcon.icns
SetFile -a C /Volumes/ClipLLM\ Installer
touch /Volumes/ClipLLM\ Installer

# Unmount the DMG
hdiutil detach /Volumes/ClipLLM\ Installer

# Convert back to read-only format
hdiutil convert ClipLLM_rw.dmg -format UDZO -o ClipLLM_final.dmg

# Clean up
rm ClipLLM_rw.dmg
```

Your final DMG file will be `ClipLLM_final.dmg`.

Note: Ensure you have the necessary permissions and sufficient disk space for these operations. If you encounter any issues, you may need to use `sudo` for some commands, but be cautious when doing so.
