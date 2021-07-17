"""Example of message encryption using the Affine cipher"""

from simple_ciphers.ciphers.affine import AffineCipher

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY_A = 7
KEY_B = 47

cipher = AffineCipher()
encrypted_text = cipher.encrypt(MESSAGE_TO_ENCRYPT, KEY_A, KEY_B)

print(encrypted_text)
