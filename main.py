# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.login_screen import LoginScreen
from vault.password_vault import init_db


def run_app():
    init_db()
    app = QApplication(sys.argv)
    login_window = LoginScreen()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()