# Screen Rotator

**English** | [Русский](README.md)

Simple utility to rotate screen by 180° using hotkeys. Runs in Windows system tray.

## Features

- 🔄 Rotate screen by 180° and back
- ⌨️ Hotkey support: **Ctrl+Alt+R**
- 🔽 Minimize to system tray
- 📊 Current status display in tray
- 🚪 Exit via tray menu

## Installation

### Pre-built exe (Releases)
Download `ScreenRotator.exe` from [Releases](../../releases)

### From source
```bash
git clone https://github.com/yourusername/screen-rotator.git
cd screen-rotator
pip install -r requirements_build.txt
python screen_rotator.py
```

## Build to exe

```bash
python build.py
```

The executable will appear in `dist/ScreenRotator.exe`

## Requirements

- Windows 10/11
- Python 3.7+ (only for running from source)

## Usage

1. Run the application
2. It will minimize to tray
3. **Ctrl+Alt+R** - rotate screen
4. Click tray icon - view status
5. Right click → Exit - close application

## License

MIT