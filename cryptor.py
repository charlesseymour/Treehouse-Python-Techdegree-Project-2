import sys

from caesar import Caesar
from atbash import Atbash
from polybius import Polybius
from transposition import Transposition


def crypt():
    """Allows the user to pick a cipher system, choose between encryption
    and decryption, and enter text.  Encrypted/decrypted text will be returned.
    """
    selection = None
    mode = None
    text = None
    ciphers_dict = {'1': Atbash, '2': Polybius, '3': Transposition}
    menu = """Choose among the following ciphers by entering the corresponding number: 

            1 - Atbash
            2 - Polybius square
            3 - Transposition (Rail Fence)
            
    Enter m to repeat this menu or q to quit"""
    print(menu)
    #User chooses cipher system
    while selection == None:
      selection = input('>>')
      if selection not in ['1', '2', '3']:
        if selection == 'm':
          print(menu)
          selection = None
        elif selection == 'q':
          sys.exit(0)
        else:
          print("Enter 1, 2, or 3 for the corresponding cipher (m=menu, q=quit)")
          selection = None
    #User chooses either encryption or decryption
    mode_select = "Enter e for encrypt or d for decrypt (q=quit)"
    while mode == None:
      mode = input(mode_select + '>>')
      if mode.lower() not in ['e', 'd']:
        if mode.lower() == 'q':
          sys.exit(0)
        else:
          mode = None
    #User inputs text to be encrypted/decrypted
    text_input = "Enter the text to be {}ed.".format('encrypt' if mode.lower() == 'e' else 'decrypt')
    while text == None or text == '' or text.isspace():
      text = input(text_input + '>>')
    #Text is run through selected cipher and encrypted/decrypted text is #outputted
    method = ciphers_dict[selection]()
    print("The {}ed text is: {}".format(
            'encrypt' if mode.lower() == 'e'
            else 'decrypt', 
            method.encrypt(text) if mode.lower() == 'e'
            else method.decrypt(text))
          )
 
 
#run crypt and allow user to repeat process   
again = 'Y'
while again != 'N':    
    crypt()
    again = input("Encrypt/decrypt another message? (Y/n)").upper()

    
