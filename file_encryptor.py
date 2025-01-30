from Crypto.Cipher import AES
import os

def pad(text):
    return text + ' ' * (16 - len(text) % 16)

def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(filename, 'rb') as file:
        plaintext = file.read()
    encrypted = cipher.encrypt(pad(plaintext.decode()).encode())
    with open(filename + ".enc", 'wb') as file:
        file.write(encrypted)

def decrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(filename, 'rb') as file:
        encrypted = file.read()
    decrypted = cipher.decrypt(encrypted).decode().strip()
    with open(filename.replace(".enc", "_decrypted.txt"), 'w') as file:
        file.write(decrypted)

key = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes
encrypt_file("test.txt", key)
decrypt_file("test.txt.enc", key)
