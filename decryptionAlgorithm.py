"""
    Created: 26.01.2021
    Author: StefanN
    Email: stefannistea@yahoo.com
    
    Last modified by: StefanN (stefannistea@yahoo.com)
    Last modified date: 19.06.2023
    
    Required package: pycryptodome

    Scope: create decryption method
    Input: ciphertext
    Output: plaintext
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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
    
    # byte string with double \
    bytes_ciphertext_doubled = ciphertext.encode()
    
    # get the correct byte string 
    try:
        bytes_ciphertext = bytes_ciphertext_doubled.decode('unicode-escape').encode('ISO-8859-1')
        # e.g: b'O\\x8c\\x90\\x05\\xa1\\xe2!\\xbe' becomes b'O\x8c\x90\x05\xa1\xe2!\xbe'
        # https://stackoverflow.com/a/33258055
    except UnicodeDecodeError:
        plaintext = "Something went wrong. Error_code: 1" \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext
    
    # decrypt data
    try:
        padded_plaintext_bytes = cipher.decrypt(bytes_ciphertext)
    except ValueError:
        plaintext = "Something went wrong. Error_code: 2" \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext
    
    # Remove the padding from the decrypted plaintext
    try:
        unpadded_data = unpad(padded_plaintext_bytes, AES.block_size)
    except:
        plaintext = "Something went wrong. Error_code: 3" \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext
        
    # utf-8 to normal text
    try:
        plaintext = unpadded_data.rstrip().decode("utf-8")
    except:
        plaintext = "Something went wrong. Error_code: 4" \
                    "\nDo you have the right message? " \
                    "\nDo you have the right password?"
        return plaintext

    return plaintext
