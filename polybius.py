import string
import math

from ciphers import Cipher


class Polybius(Cipher):

    def __init__(self):
        """Assigns uppercase alphabet (minus 'J') as a single string
        to self.alphabet, to be used by encrypt/decrypt methods.
        """
        #'J' is removed so that alphabet maps onto 5x5 grid
        self.alphabet = string.ascii_uppercase.replace("J", '')

    def encrypt(self, text):
        """Takes text and encrypts it according to the Polybius method."""
        output = []
        text = text.upper()
        for char in text:
            if char == "J":
              char = "I"
            try:
                digit1 = str(math.ceil((self.alphabet.index(char) + 1) / 5))
                digit2 = str((self.alphabet.index(char) % 5) + 1)
                digits =  digit1 + digit2
            except ValueError:
                continue
            else:
                output.append(digits)
        return ''.join(output)

    def decrypt(self, text):
        """Takes text and decrypts it according to the Polybius method."""
        output = []
        text = text.strip()
        while len(text):
            try:
                abc_index = (int(text[0]) * 5) - (5 - int(text[1])) - 1
            except ValueError:
                continue
            else:
                output.append(self.alphabet[abc_index])
            text = text[2:]
        return ''.join(output)
 

