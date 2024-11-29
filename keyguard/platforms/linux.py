# keyguard/platforms/linux.py
from Xlib import X, XK, display
from Xlib.protocol import event
import threading

class LinuxKeyboardHandler:
    def __init__(self):
        self.display = display.Display()
        self.root = self.display.screen().root
        self.running = False
        
    def check_permissions(self) -> bool:
        try:
            self.root.grab_keyboard(True, X.GrabModeAsync, X.GrabModeAsync, X.CurrentTime)
            self.root.ungrab_keyboard(X.CurrentTime)
            return True
        except:
            return False
            
    def start_protection(self):
        self.running = True
        self._protection_thread = threading.Thread(target=self._protect_keyboard)
        self._protection_thread.daemon = True
        self._protection_thread.start()
        
    def stop_protection(self):
        self.running = False
        
    def _protect_keyboard(self):
        while self.running:
            try:
                self.root.change_attributes(event_mask=X.KeyPressMask)
                self.display.sync()
            except:
                continue
            
