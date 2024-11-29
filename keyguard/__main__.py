import sys
from keyguard.cli import main as cli_main
from keyguard.gui import main as gui_main

def main():
    print("Welcome to Keyguard!")
    print("Please select a mode:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        print("Starting CLI mode...")
        sys.exit(cli_main())
    elif choice == "2":
        print("Starting GUI mode...")
        sys.exit(gui_main())
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
