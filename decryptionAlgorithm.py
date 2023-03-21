"""
    Created: 26.01.2021
    Author: Artaao
    Email: Artaao@protonmail.com
    
    Last modified by: Artaao (Artaao@protonmail.com)
    Last modified date: 21.03.2023
    
    Required package: pycryptodome

    Scope: create decryption method
    Input: ciphertext
    Output: plaintext
"""

from Crypto.Cipher import AES
import hashlib


def decrypt(ciphertext, cipherkey):
    # input:
    # bytes of the ciphertext in str type, without b ' '
    # cipherkey as str

    EncodedCipherkey = cipherkey.encode()  # Turns it in bytes
    key = hashlib.sha256(EncodedCipherkey).digest()  # creates 32 byte key

    mode = AES.MODE_CBC  # Cypher Block Chain

    # ---------- NOTE ----------
    # IV changed for improved "ED: Encryption - Decryption" app security
    # --------------------------
    IV = "0123456789012345".encode()  # len(IV) == 16

    cipher = AES.new(key, mode, IV)
    bytes_ciphertext_doubled = ciphertext.encode()
    try:
        bytes_ciphertext = bytes_ciphertext_doubled.decode('unicode-escape').encode('ISO-8859-1')
        # https://stackoverflow.com/a/33258055
    except UnicodeDecodeError:
        plaintext = "Something went wrong." \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext

    try:
        padded_plaintext_bytes = cipher.decrypt(bytes_ciphertext)
    except ValueError:
        plaintext = "Something went wrong." \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext
    try:
        plaintext = padded_plaintext_bytes.rstrip().decode()
    except:
        plaintext = "Something went wrong." \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext

    return plaintext
