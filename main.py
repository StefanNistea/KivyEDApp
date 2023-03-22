"""
    Created: 06.03.2021
    Author: Artaao
    Email: Artaao@protonmail.com

    Last modified by: Artaao (Artaao@protonmail.com)
    Last modified date: 22.03.2023
    
    Required package: kivy
    Required files: decryptionAlgorithm.py, encryptionAlgorithm.py, my.kv
    
    Scope: App entry point | Initialize Kivy framework
"""

# install all requrements.txt first
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.clipboard import Clipboard
from kivy.uix.label import Label

import encryptionAlgorithm
import decryptionAlgorithm


class Data:
    def __init__(self, encryptionKey, decryptionKey):
        self.encryptionKey = encryptionKey
        self.decryptionKey = decryptionKey

    def get_encpass(self):
        return self.encryptionKey

    def get_decpass(self):
        return self.decryptionKey


# dc is an object that contains encryption keys (encryption key, decryption key)
dc = Data("someRandomKey","someRandomKey")

class InitWindow(Screen):
    pass

class MainWindow(Screen):

    def releaseButton(self):
        import webbrowser
        self.ids.bmcImage.source = "resources/bmcButton.png"
        webbrowser.open('https://www.buymeacoffee.com/Artaao')
            
    def pressButton(self):
        self.ids.bmcImage.source = "resources/bmcButtonOnPress.png"

class SecondWindow(Screen):  # Encryption password request

    def enc(self):
        encryptionKey = ObjectProperty(None)
        dc.encryptionKey = self.encryptionKey.text
        
    def changeScreenAction(self):
        # restes the password if any
        dc.decryptionKey = "someRandomKey"
        dc.encryptionKey = "someRandomKey"
        
        # input field emptied
        self.ids.encryptionKey.text = ""


class ThirdWindow(Screen):  # Decryption password request

    def dec(self):
        decryptionKey = ObjectProperty(None)
        dc.decryptionKey = self.decryptionKey.text
        
    def changeScreenAction(self):
        # restes the password if any
        dc.decryptionKey = "someRandomKey"
        dc.encryptionKey = "someRandomKey"
        
        # input field emptied
        self.ids.decryptionKey.text = ""


class ForthWindow(Screen):  # Encryption screen

    plaintext = ObjectProperty(None)
    key = "someRandomKey"
    ciphertext = ""

    def encode(self):
        self.key = dc.get_encpass()
        
        try:
            self.ciphertext = encryptionAlgorithm.encrypt(self.plaintext.text, self.key)  # Output: b' [bytes] '
            # b ' ' must be deleted in the next two lines.
            self.ciphertext = str(self.ciphertext)
            self.ciphertext = self.ciphertext[2:-1]
        except ValueError:
            self.ciphertext = "Images and emojis are not supported yet"

        self.ids.encrypted.text = self.ciphertext

    def changeScreenAction(self):
        # restes the password
        dc.decryptionKey = "someRandomKey"
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.encrypted.text = "" # "The ciphertext will be displayed here"
        self.ids.plaintext.text = "" # "Insert the plaintext here"
        
    def changeScreenToDecryption(self):
        # set the decryption password to be the same as the encryption one 
        dc.decryptionKey = dc.get_encpass()
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.encrypted.text = "" # "The ciphertext will be displayed here"
        self.ids.plaintext.text = "" # "Insert the plaintext here"
    
    def changeScreenToWelcome(self):
        # restes the password if any
        dc.decryptionKey = "someRandomKey"
        dc.encryptionKey = "someRandomKey"
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.encrypted.text = "" #"The ciphertext will be displayed here"
        self.ids.plaintext.text = "" #"Insert the plaintext here"
        
    def addToClipboard(self, text):
        Clipboard.copy(text)
        
    def takeFromClipboard(self):
        self.ids.plaintext.text = Clipboard.paste()
                

class FifthWindow(Screen):  # Decryption screen
    ciphertext = ObjectProperty(None)
    key = "someRandomKey"
    plaintext = " "

    def decode(self):
        self.key = dc.get_decpass()
        self.plaintext = decryptionAlgorithm.decrypt(str(self.ciphertext.text), str(self.key))

        self.ids.decrypted.text = str(self.plaintext)

    def changeScreenAction(self):
        # resets the password 
        dc.encryptionKey = "someRandomKey"
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.decrypted.text = "" #"If the password is correct, the plaintext will be shown here"
        self.ids.ciphertext.text = "" #"Insert ciphertext here"
        
    def changeScreenToEncryption(self):
        # set the encryption password to be the same as the decryption one 
        dc.encryptionKey = dc.get_decpass()
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.decrypted.text = "" # "If the password is correct, the plaintext will be shown here"
        self.ids.ciphertext.text = "" # "Insert ciphertext here"
     
    def changeScreenToWelcome(self):
        # restes the password if any
        dc.decryptionKey = "someRandomKey"
        dc.encryptionKey = "someRandomKey"
        
        # the following two lines reset the text displayed in both text boxes when the screen is changed
        self.ids.decrypted.text = "" # "If the password is correct, the plaintext will be shown here"
        self.ids.ciphertext.text = "" # "Insert ciphertext here"
        
    def addToClipboard(self, text):
        Clipboard.copy(text)
        
    def takeFromClipboard(self):
        self.ids.ciphertext.text = Clipboard.paste()

    
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class EDApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    EDApp().run()
