# ui/login_screen.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from auth.pin_auth import validate_pin
from ui.vault_screen import VaultScreen
from biometric.fingerprint import authenticate_with_fingerprint


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login - Secure Vault')

        self.label = QLabel('Enter PIN:')
        self.pin_input = QLineEdit()
        self.pin_input.setEchoMode(QLineEdit.Password)

        self.button = QPushButton('Unlock')
        self.button.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pin_input)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def handle_login(self):
        if authenticate_with_fingerprint():
            self.vault_window = VaultScreen()
            self.vault_window.show()
            self.close()
        else:
            # fallback to PIN
            pin = self.pin_input.text()
            if validate_pin(pin):
                self.vault_window = VaultScreen()
                self.vault_window.show()
                self.close()
            else:
                print("Wrong PIN")
