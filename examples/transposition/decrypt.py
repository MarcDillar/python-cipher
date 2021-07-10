"""Example of message decryption using the Simple Transposition cipher"""

from simple_ciphers.ciphers.transposition import SimpleTranspositionCipher

MESSAGE_TO_DECRYPT = "Tiehg!iisn ails  mmeys soarg"
KEY = 13

cipher = SimpleTranspositionCipher()

decrypted_message = cipher.decrypt(message=MESSAGE_TO_DECRYPT, key=KEY)
print(decrypted_message)
