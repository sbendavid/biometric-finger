from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem
from vault.password_vault import add_credential, get_all_credentials

class VaultScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vault Dashboard')
        self.resize(600, 400)

        # Input fields
        self.site_input = QLineEdit()
        self.site_input.setPlaceholderText('Site')

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText('Username')

        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText('Password')

        # Buttons
        self.add_btn = QPushButton('Add Credential')
        self.add_btn.clicked.connect(self.save_credential)

        # Table to show credentials
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Site', 'Username', 'Password'])

        # Layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.site_input)
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.pass_input)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_credentials()

    def save_credential(self):
        site = self.site_input.text()
        username = self.user_input.text()
        password = self.pass_input.text()

        if site and username and password:
            add_credential(site, username, password)
            self.site_input.clear()
            self.user_input.clear()
            self.pass_input.clear()
            self.load_credentials()

    def load_credentials(self):
        creds = get_all_credentials()
        self.table.setRowCount(0)
        for row_idx, (site, user, password) in enumerate(creds):
            self.table.insertRow(row_idx)
            self.table.setItem(row_idx, 0, QTableWidgetItem(site))
            self.table.setItem(row_idx, 1, QTableWidgetItem(user))
            self.table.setItem(row_idx, 2, QTableWidgetItem(password))