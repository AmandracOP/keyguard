# keyguard/cli.py
import argparse
import sys
import time
from .core.prevention import KeyguardMonitor

def main():
    parser = argparse.ArgumentParser(description="Keyguard - Keylogger Prevention Tool")
    parser.add_argument("--no-gui", action="store_true", help="Run in CLI mode")
    args = parser.parse_args()
    
    if not args.no_gui:
        from .gui import main as gui_main
        gui_main()
        return
        
    monitor = KeyguardMonitor()
    
    def log_callback(message: str):
        print(f"[Keyguard] {message}")
        
    try:
        print("Starting Keyguard protection...")
        monitor.start_monitoring(log_callback)
        print("Protection active. Press Ctrl+C to stop.")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping Keyguard protection...")
        monitor.stop_monitoring()
        print("Protection stopped.")
        sys.exit(0)
        
    except PermissionError as e:
        print(f"Error: {str(e)}")
        print("Please run the program with appropriate privileges.")
        sys.exit(1)

if __name__ == "__main__":
    main()
