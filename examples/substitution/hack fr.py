"""
Example of message dictionary decryption
of a non-English message encrypted with a Simple Substitution cipher
"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher
from simple_ciphers.hackers.substitution import SimpleSubstitutionCipherHacker


cipher = SimpleSubstitutionCipher()
hacker = SimpleSubstitutionCipherHacker(language="fr")

MESSAGE_TO_ENCRYPT = """Tous les êtres humains naissent libres et égaux en dignité
et en droits. Ils sont doués de raison et de conscience et doivent agir les
uns envers les autres dans un esprit de fraternité."""

KEY = cipher.generate_random_key()

print(f"Original message:\n{MESSAGE_TO_ENCRYPT}\n\n")

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(f"Key:\n{KEY}\n\n")
print(f"Encrypted message:\n{encrypted_message}\n\n")

decrypted_message = hacker.hack(encrypted_message)
print(f"Decrypted message:\n{decrypted_message}")
