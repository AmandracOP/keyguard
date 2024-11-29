# keyguard/gui.py
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QPushButton, QTextEdit, QLabel)
from PyQt6.QtCore import Qt, pyqtSlot
import sys
from .core.prevention import KeyguardMonitor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyguard - Keylogger Prevention Tool")
        self.setMinimumSize(600, 400)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Status label
        self.status_label = QLabel("Status: Stopped")
        layout.addWidget(self.status_label)
        
        # Log display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        layout.addWidget(self.log_display)
        
        # Control buttons
        self.start_button = QPushButton("Start Protection")
        self.start_button.clicked.connect(self.start_protection)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("Stop Protection")
        self.stop_button.clicked.connect(self.stop_protection)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        # Initialize monitor
        self.monitor = KeyguardMonitor()
        
    @pyqtSlot()
    def start_protection(self):
        try:
            self.monitor.start_monitoring(self.log_message)
            self.status_label.setText("Status: Running")
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
        except PermissionError as e:
            self.log_message(f"Error: {str(e)}")
            
    @pyqtSlot()
    def stop_protection(self):
        self.monitor.stop_monitoring()
        self.status_label.setText("Status: Stopped")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        
    def log_message(self, message: str):
        self.log_display.append(message)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()