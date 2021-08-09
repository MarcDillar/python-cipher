"""
Example of decryption
of a message encrypted with a Vigenere cipher
with an unknown cipher key
"""

from simple_ciphers.ciphers.vigenere import VigenereCipher
from simple_ciphers.hackers.vigenere import VigenereCipherHacker


cipher = VigenereCipher()
hacker = VigenereCipherHacker()

MESSAGE_TO_ENCRYPT = """All human beings are born free and equal in dignity and rights.
They are endowed with reason and conscience and should act
towards one another in a spirit of brotherhood.
Everyone is entitled to all the rights and freedoms set forth in this Declaration,
without distinction of any kind, such as race, colour, sex, language, religion, political
or other opinion, national or social origin, property, birth or other status.
Furthermore, no distinction shall be made on the basis of the political,
jurisdictional or international status of the country or territory to which a person
belongs, whether it be independent, trust, non-self-governing or
under any other limitation of sovereignty.
Everyone has the right to life, liberty and security of person.
No one shall be held in slavery or servitude; slavery and the slave trade
shall be prohibited in all their forms.
No one shall be subjected to torture or to cruel, inhuman or degrading
treatment or punishment. Everyone has the right to recognition everywhere as a person before the law."""

KEY = "ab cd"


print(f"Original message:\n{MESSAGE_TO_ENCRYPT}\n\n")

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(f"Key:\n{KEY}\n\n")
print(f"Encrypted message:\n{encrypted_message}\n\n")

decrypted_message = hacker.hack(encrypted_message)
print(f"Decrypted message:\n{decrypted_message[:5]}")
pass
