import platform
from typing import Union

# Always import Linux handler
from .linux import LinuxKeyboardHandler

# Initialize the Windows handler to None initially
WindowsKeyboardHandler = None

try:
    # Only import the Windows handler if the system is Windows
    if platform.system() == 'Windows':
        from .windows import WindowsKeyboardHandler
except ImportError:
    pass  # Windows import fails gracefully

def get_platform_handler() -> Union[LinuxKeyboardHandler, WindowsKeyboardHandler]:
    """Return the appropriate platform-specific handler"""
    system = platform.system()
    if system == 'Linux':
        return LinuxKeyboardHandler()
    elif system == 'Windows' and WindowsKeyboardHandler is not None:
        return WindowsKeyboardHandler()
    else:
        raise NotImplementedError(f"Platform {system} is not supported")
