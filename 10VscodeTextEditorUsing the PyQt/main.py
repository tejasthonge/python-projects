import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QPalette, QColor

class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VS Code Clone")
        self.setGeometry(100, 100, 800, 600)

        # Set a dark color scheme similar to VS Code
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, QColor(187, 187, 187))
        palette.setColor(QPalette.Base, QColor(42, 42, 42))
        palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ToolTipBase, QColor(187, 187, 187))
        palette.setColor(QPalette.ToolTipText, QColor(30, 30, 30))
        palette.setColor(QPalette.Text, QColor(187, 187, 187))
        palette.setColor(QPalette.Button, QColor(70, 70, 70))
        palette.setColor(QPalette.ButtonText, QColor(187, 187, 187))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(56, 252, 196))
        palette.setColor(QPalette.Highlight, QColor(56, 252, 196))
        palette.setColor(QPalette.HighlightedText, QColor(30, 30, 30))

        self.setPalette(palette)

        self.text_edit = QTextEdit(self)
        self.text_edit.setStyleSheet("background-color: #2E2E2E; color: #B7B7B7; border: none;")
        self.text_edit.setPlaceholderText("Write your code here...")

        self.open_button = QPushButton("Open File", self)
        self.open_button.setStyleSheet("background-color: #464646; color: #B7B7B7; border: none;")
        self.open_button.clicked.connect(self.open_file)

        self.save_button = QPushButton("Save File", self)
        self.save_button.setStyleSheet("background-color: #464646; color: #B7B7B7; border: none;")
        self.save_button.clicked.connect(self.save_file)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.open_button)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_edit.setPlainText(content)

    def save_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())

def main():
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
