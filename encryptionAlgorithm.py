"""
    Created: 26.01.2021
    Author: StefanN
    Email: stefannistea@yahoo.com
    
    Last modified by: StefanN (stefannistea@yahoo.com)
    Last modified date: 19.06.2023
    
    Required package: pycryptodome
    
    Scope: create encryption method
    Input: plaintext
    Output: ciphertext
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 
import hashlib


def encrypt(plaintext, cipherkey):

    EncodedCipherkey = cipherkey.encode()  # Turns it in bytes
    key = hashlib.sha256(EncodedCipherkey).digest()  # creates 32 byte key

    mode = AES.MODE_CBC  # Cypher Block Chain
    
    # ---------- NOTE ----------
    # IV changed for improved "ED: Encryption - Decryption" app security
    # --------------------------
    IV = "0123456789012345".encode()  # len(Init Vector) == 16

    cipher = AES.new(key, mode, IV)

    # Apply PKCS7 padding to the plaintext
    padded_plaintext = pad(plaintext.encode("utf-8"), AES.block_size)

    ciphertext = cipher.encrypt(padded_plaintext)

    return ciphertext
