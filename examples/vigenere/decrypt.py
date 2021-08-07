"""Examples of message encryption using the Vigenere cipher"""

from simple_ciphers.ciphers.vigenere import VigenereCipher

key = "This is my cipher key"

cipher = VigenereCipher()
message = "Alzw ia lhq keuapni khkx ubst te mfcdwpvms."
decrypted_message = cipher.decrypt(message, key)
print(decrypted_message)
