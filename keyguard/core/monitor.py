import os
import psutil
import threading
import time
from typing import Callable, Set

class ProcessMonitor:
    def __init__(self, callback: Callable[[str], None]):
        """
        Initialize the ProcessMonitor class.
        
        :param callback: A function that will be called when a suspicious process is detected.
        """
        self.callback = callback
        self.suspicious_processes: Set[int] = set()
        self._stop_event = threading.Event()

    def start(self):
        """Start the process monitoring in a separate thread."""
        if not self.check_permissions():
            raise PermissionError("Insufficient permissions to monitor processes. Ensure the script has elevated privileges.")
        
        # Start the monitoring thread
        self._monitor_thread = threading.Thread(target=self._monitor_loop)
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        
    def stop(self):
        """Stop the monitoring thread."""
        self._stop_event.set()

    def _monitor_loop(self):
        """Loop that monitors processes periodically."""
        while not self._stop_event.is_set():
            try:
                # Iterate over all running processes
                for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                    proc_info = proc.info
                    # Check if the process is suspicious
                    if self._is_suspicious(proc_info):
                        if proc.pid not in self.suspicious_processes:
                            self.suspicious_processes.add(proc.pid)
                            self.callback(f"Suspicious process detected: {proc_info['name']} (PID: {proc.pid})")
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                # Handle permission errors or process termination
                continue
            except Exception as e:
                # Handle other unexpected errors
                print(f"Error during process monitoring: {e}")
            time.sleep(1)

    def _is_suspicious(self, proc_info: dict) -> bool:
        """Check if the process name or command line contains suspicious keywords."""
        suspicious_keywords = ['keylog', 'hook', 'spy', 'capture']
        name = proc_info['name'].lower() if proc_info['name'] else ''
        cmdline = ' '.join(proc_info['cmdline']).lower() if proc_info['cmdline'] else ''
        
        return any(keyword in name or keyword in cmdline for keyword in suspicious_keywords)

    def check_permissions(self) -> bool:
        """Check if the current user has permission to monitor processes."""
        # Ensure the script has the necessary permissions to inspect all processes
        return os.geteuid() == 0  # Check if running as root (UID 0) on Linux
