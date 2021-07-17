"""Example of message encryption using the Affine cipher"""

from simple_ciphers.ciphers.affine import AffineCipher

MESSAGE_TO_DECRYPT = "w%,H5,H5O%J51JHHhXJ5O%hO5*,  5oJ5J8vA\mOJC"
KEY_A = 7
KEY_B = 47

cipher = AffineCipher()
decrypted_text = cipher.decrypt(MESSAGE_TO_DECRYPT, KEY_A, KEY_B)

print(decrypted_text)