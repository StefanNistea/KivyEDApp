"""
    Created: 26.01.2021
    Author: Artaao
    Email: Artaao@protonmail.com
    
    Last modified by: Artaao (Artaao@protonmail.com)
    Last modified date: 21.03.2023
    
    Required package: pycryptodome
    
    Scope: create encryption method
    Input: plaintext
    Output: ciphertext
"""

from Crypto.Cipher import AES
import hashlib


def pad_message(message):
    while len(message) % 16 != 0:
        message = message + " "
    return message


def encrypt(plaintext, cipherkey):

    EncodedCipherkey = cipherkey.encode()  # Turns it in bytes
    key = hashlib.sha256(EncodedCipherkey).digest()  # creates 32 byte key

    mode = AES.MODE_CBC  # Cypher Block Chain
    
    # ---------- NOTE ----------
    # IV changed for improved "ED: Encryption - Decryption" app security
    # --------------------------
    IV = "0123456789012345".encode()  # len(Init Vector) == 16

    cipher = AES.new(key, mode, IV)

    # The input message has to be in 16-byte length chunks
    padded_plaintext = pad_message(plaintext)

    padded_plaintext_bytes = padded_plaintext.encode()

    ciphertext = cipher.encrypt(padded_plaintext_bytes)

    return ciphertext
