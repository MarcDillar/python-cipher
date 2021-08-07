"""Examples of message decryption using the Affine cipher"""

from simple_ciphers.ciphers.affine import AffineCipher

KEY_A = 7
KEY_B = 47

# Cipher using simple mode
message_to_decrypt = "Yszr zr ysx bxrrvlx ysvy tzuu cx xijkhwyxq"
cipher = AffineCipher()
decrypted_text = cipher.decrypt(message_to_decrypt, KEY_A, KEY_B)

print(decrypted_text)

# Cipher using all ASCII Printable characters
message_to_decrypt = "w%,H5,H5O%J51JHHhXJ5O%hO5*,  5oJ5J8vA\mOJC"
cipher = AffineCipher(simple=False)
decrypted_text = cipher.decrypt(message_to_decrypt, KEY_A, KEY_B)

print(decrypted_text)
