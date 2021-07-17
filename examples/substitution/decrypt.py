"""Example of message decryption using the Simple Substitution cipher"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher

MESSAGE_TO_DECRYPT = "Iaca sr jia narrlua jilj xaaor jp fa axwchbjao"
KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

cipher = SimpleSubstitutionCipher()

decrypted_message = cipher.decrypt(message=MESSAGE_TO_DECRYPT, key=KEY)
print(decrypted_message)
