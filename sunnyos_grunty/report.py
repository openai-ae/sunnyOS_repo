import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from os import system, path
from pathlib import Path

class ErrorReporterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Set up the layout
        QMessageBox.warning(self, "Warning", "Anthropic Api Key is missing.\nOpening api manager...")
        layout = QVBoxLayout()

        # Create a QLineEdit for inputting the error message
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter Anthropic API Key:")
        layout.addWidget(self.line_edit)

        # Create a QPushButton to trigger the error report
        report_button = QPushButton("Push", self)
        report_button.clicked.connect(self.on_submit)
        layout.addWidget(report_button)

        # Set the layout for the dialog
        self.setLayout(layout)

        # Set dialog properties
        self.setWindowTitle("Enter Your API Key")
        self.setGeometry(100, 100, 300, 100)

    def on_submit(self):
        """
        Handles the submit button click.
        """
        # Get the error message from the QLineEdit
        error_msg = self.line_edit.text()
        api_path = Path.home() / ".grunty" / ".api"
        system("mkdir -p ~/.grunty")

        try:     
            with open(api_path, "w") as api:
                api.write(error_msg)
                api.close()
        except Exception as e:
            QMessageBox.critical(self, "Crititcal Error", f"an Unknown critical error happened with the message:\n{e}")
            exit(1)
        QMessageBox.information(self, "Ok", "API Key is saved, restart grunty to take effect.")
        exit(0)
        
    def report_error(self, msg):
        """
        Displays an error message in a QMessageBox.
        :param msg: The error message to display.
        """
        # Show the error message in a QMessageBox
        # QMessageBox.critical(self, "Error", msg)

def setup_api():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    dialog = ErrorReporterDialog()
    dialog.report_error("n")
    dialog.exec()

