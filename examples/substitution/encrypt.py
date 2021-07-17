"""Example of message encryption using the Simple Substitution cipher"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher

MESSAGE_TO_ENCRYPT = "Here is the message that needs to be encrypted"
KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

cipher = SimpleSubstitutionCipher()

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(encrypted_message)
