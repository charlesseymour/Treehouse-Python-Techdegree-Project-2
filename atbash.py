import string

from ciphers import Cipher


class Atbash(Cipher):

    def __init__(self):
        """Assigns the uppercase alphabet as a single string to 
        self.alphabet, to be used by encrypt/decrypt methods.
        """
        self.alphabet = string.ascii_uppercase

    def encrypt(self, text):
        """Takes text and encrypts it according to the Atbash method."""
        output = []
        text = text.upper()
        for char in text:
            try:
                index = self.alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alphabet[25 - index])
        return ''.join(output)

    def decrypt(self, text):
        """Takes text and decrypts it according to the Atbash method."""
        #Atbash merely switches letter positions so encrypt and decrypt
        #methods are the same
        return self.encrypt(text)
      
