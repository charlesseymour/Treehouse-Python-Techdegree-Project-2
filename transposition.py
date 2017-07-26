import string
import math

from ciphers import Cipher


class Transposition(Cipher):

    def __init__(self):
        """Assigns the uppercase alphabet as a single string to 
        self.alphabet, to be used by encrypt/decrypt methods.
        """
        self.alphabet = string.ascii_uppercase

    def encrypt(self, text):
        """Takes text and encrypts it according to the Rail Fence method.
        """
        text = text.upper()
        #create the three rails
        first_rail = ''
        second_rail = ''
        third_rail = ''
        #loop through text and assign characters to rails
        current_index = 0
        for char in text:
            if current_index % 4 == 0:
                first_rail += char
            elif (current_index + 1) % 2 == 0:
                second_rail += char
            else:
                third_rail += char
            current_index += 1  
        #encrypted text is concatenation of rails
        return first_rail + second_rail + third_rail

    def decrypt(self, text):
        """Takes text and decrypts it according to the Rail Fence method.
        """
        output = ''
        text = text.upper()
        #create three rails
        first_rail = ''
        second_rail = ''
        third_rail = ''
        #determine how long the rails should be given the length of the 
        #encrypted text.  Third rail will be the characters remaining after first and second rail.
        first_rail_length = (math.floor(len(text) / 4) 
                            + math.ceil(((len(text) % 4) / 4)))
        second_rail_length = ((math.floor(len(text) / 4) * 2) 
                             + math.floor(((len(text) % 4) / 2)))
        #loop through text and assign character to correct rail
        count = 0
        while count < len(text):
            if count < first_rail_length:
                first_rail += text[count]
            elif count < second_rail_length + first_rail_length:
                second_rail += text[count]
            else:
                third_rail += text[count]
            count += 1
        #decrypt text by going through rail elements in correct order
        count = 0
        while count < len(text):
            if count % 4 == 0:
                output += first_rail[int(count / 4)]
            elif ((count % 4) % 2) != 0:
                output += second_rail[math.floor(count / 2)]
            else:
                output += third_rail[int((count - 2) / 4)]
            count += 1
        return output