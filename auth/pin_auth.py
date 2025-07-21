# auth/pin_auth.py
import hashlib

def validate_pin(input_pin):
    stored_hash = "ed946f65d2c785d90e827c5ffd879ce3b49c68d4c88013074176a7e73bc58bcf"  # Replace with real hash of PIN
    input_hash = hashlib.sha256(input_pin.encode()).hexdigest()
    return input_hash == stored_hash