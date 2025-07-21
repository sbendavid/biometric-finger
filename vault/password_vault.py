# vault/password_vault.py
import sqlite3
from vault.key_manager import load_or_create_key
from cryptography.fernet import Fernet

# In a real app, this key should be stored securely and reused
key = load_or_create_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode())

def decrypt_password(encrypted_pass):
    return cipher.decrypt(encrypted_pass).decode()

def init_db():
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password_encrypted TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_credential(site, username, password):
    encrypted = encrypt_password(password)
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO credentials (site, username, password_encrypted) VALUES (?, ?, ?)",
                   (site, username, encrypted))
    conn.commit()
    conn.close()

def get_all_credentials():
    conn = sqlite3.connect("data/vault.db")
    cursor = conn.cursor()
    cursor.execute("SELECT site, username, password_encrypted FROM credentials")
    rows = cursor.fetchall()
    conn.close()
    return [(site, username, decrypt_password(enc_pass)) for site, username, enc_pass in rows]


