import hashlib
from cryptography.fernet import Fernet

# Sabit açar
KEY = b'7u8vJX9mQ1oR4dZ8KJz6Jz1Q7KcFJm1wq5hNnqJ8Y9A='
cipher = Fernet(KEY)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    return cipher.decrypt(encrypted_message).decode()


'''import hashlib
from cryptography.fernet import Fernet

# =====================
# PASSWORD HASHING
# =====================
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# =====================
# ENCRYPTION
# =====================
cipher = Fernet(KEY)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    return cipher.decrypt(encrypted_message).decode()
'''
