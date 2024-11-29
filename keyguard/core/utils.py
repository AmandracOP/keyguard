# keyguard/core/utils.py
import os
import sys
import ctypes
from typing import Optional

def is_admin() -> bool:
    """Check if the current process has administrative privileges"""
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0

def elevate_privileges():
    """Attempt to elevate privileges if needed"""
    if not is_admin():
        if platform.system() == 'Windows':
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            print("Please run with sudo privileges")
            sys.exit(1)