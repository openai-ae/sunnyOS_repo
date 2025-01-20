import sys
import logging
from os import system
from PyQt6.QtWidgets import QApplication, QMessageBox
try: 
    from .window import MainWindow
    from .store import Store
    from .anthropic import AnthropicClient
except ModuleNotFoundError:
    QMessageBox.info(None, "Info", "SunnyOS Grunty is preparing for first use.")
    system("python3 -m pip install qtawesome numpy pillow python-dotenv anthropic requests pyautogui --break-system-packages")
    QMessageBox.info(None, "Success", "Restart SunnyOS Grunty.")
    exit(0)

logging.basicConfig(filename='agent.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    app = QApplication(sys.argv)
    
    app.setQuitOnLastWindowClosed(False)  # Prevent app from quitting when window is closed
    
    store = Store()
    anthropic_client = AnthropicClient()
    
    window = MainWindow(store, anthropic_client)
    window.show()  # Just show normally, no maximize
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
