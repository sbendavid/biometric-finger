# 🧠 Biometric Password Manager (Windows)

Secure your credentials using PIN-based authentication and optional fingerprint scanning via Windows Hello.

## 💻 Features
- AES-256 encrypted password storage (via Fernet)
- PIN-based login (hashed for security)
- Fingerprint support (via external helper)
- Local SQLite database (no cloud sync)
- Clean PyQt5 UI for adding/viewing credentials

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Project
```bash
git clone https://github.com/your-username/biometric-password-manager.git
cd biometric-password-manager
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Your PIN
`Use Python shell:`
```bash
import hashlib
pin = "2580"
hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
print(hashed_pin)
```

`Paste the hash into auth/pin_auth.py.`

🖐️ Fingerprint Setup (Optional)
If using Windows Hello:
- Compile FingerprintHelper.cs into FingerprintHelper.exe
- Place it in the project root
- The Python app will run it using subprocess
