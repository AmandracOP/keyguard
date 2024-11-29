# README.md
# Keyguard - Keylogger Prevention Tool

Keyguard is a cross-platform tool designed to detect and prevent keylogger threats on both Windows and Linux systems. It provides real-time monitoring of suspicious processes and keyboard access attempts.

## Features
- Real-time process monitoring for potential keyloggers
- Platform-specific keyboard protection
- Both GUI and CLI interfaces
- Administrative privilege handling
- Cross-platform support (Windows/Linux)

## Installation
```bash
# Clone the repository
git clone https://github.com/AmandracOP/keyguard.git
cd keyguard

# Install dependencies
pip install -e .
```

## Usage
### GUI Mode
```bash
python -m keyguard
```

### CLI Mode
```bash
python -m keyguard --no-gui
```

## Requirements
- Python 3.8+
- PyQt6 (for GUI)
- Platform-specific dependencies (see requirements.txt)

## License
MIT License