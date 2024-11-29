import os
import platform
from typing import Optional
from ..platforms import get_platform_handler

class KeyguardMonitor:
    def __init__(self):
        # Initialize platform handler based on the system platform
        self.platform_handler = get_platform_handler()
        self.process_monitor = None
        
    def start_monitoring(self, callback):
        """Start monitoring for potential keyloggers"""
        
        # Check if the platform handler confirms sufficient permissions
        if not self.platform_handler.check_permissions():
            raise PermissionError("Insufficient permissions to monitor keyboard. Ensure you are running with elevated privileges (e.g., as root).")
        
        # Start process monitoring
        self.process_monitor = ProcessMonitor(callback)
        self.process_monitor.start()
        
        # Begin platform-specific protection activities
        self.platform_handler.start_protection()
        
    def stop_monitoring(self):
        """Stop all monitoring activities"""
        
        # Stop process monitoring if active
        if self.process_monitor:
            self.process_monitor.stop()
        
        # Stop platform-specific protection activities
        self.platform_handler.stop_protection()
