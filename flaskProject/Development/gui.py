import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, \
    QLabel, QHBoxLayout, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Uploader")

        # Title text
        self.title_label = QLabel("File Uploader")
        self.title_label.setAlignment(Qt.AlignCenter)

        # Upload File button
        self.upload_button = QPushButton("Upload File")
        self.upload_button.clicked.connect(self.upload_file)

        # Clear button
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)

        # Chat window
        self.chat_window = QTextEdit()

        # Additional text area
        self.additional_text_area = QTextEdit()

        # Text input area
        self.text_input = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.upload_button)
        left_layout.addWidget(self.clear_button)
        left_layout.addWidget(self.chat_window)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.additional_text_area)
        right_layout.addWidget(self.text_input)
        right_layout.addWidget(self.send_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            # Logic to handle file upload
            # For demonstration, simply display the file path in the chat window
            self.chat_window.append("File uploaded: " + file_path)

    def clear_text(self):
        self.chat_window.clear()

    def send_message(self):
        message = self.text_input.text()
        if message:
            self.additional_text_area.append("You: " + message)
            self.text_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
