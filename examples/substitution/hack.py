"""
Example of message dictionary decryption
of a message encrypted with a Simple Substitution cipher
"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher
from simple_ciphers.hackers.substitution import SimpleSubstitutionCipherHacker


cipher = SimpleSubstitutionCipher()
hacker = SimpleSubstitutionCipherHacker()

MESSAGE_TO_ENCRYPT = """All human beings are born free and equal in dignity and rights.
They are endowed with reason and conscience and should act
towards one another in a spirit of brotherhood."""

KEY = cipher.generate_random_key()

print(f"Original message:\n{MESSAGE_TO_ENCRYPT}\n\n")

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(f"Key:\n{KEY}\n\n")
print(f"Encrypted message:\n{encrypted_message}\n\n")

decrypted_message = hacker.hack(encrypted_message)
print(f"Decrypted message:\n{decrypted_message}")
