"""Example of message encryption using the Simple Substitution cipher"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher

MESSAGE_TO_ENCRYPT = "Here is the message that needs to be encrypted"
cipher = SimpleSubstitutionCipher()

# Encryption with a key
KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(encrypted_message)

# Encryption with a mapping dictionnary
MAPPING = {
        "A": "L",
        "B": "F",
        "C": "W",
        "D": "O",
        "E": "A",
        "F": "Y",
        "G": "U",
        "H": "I",
        "I": "S",
        "J": "V",
        "K": "K",
        "L": "M",
        "M": "N",
        "N": "X",
        "O": "P",
        "P": "B",
        "Q": "D",
        "R": "C",
        "S": "R",
        "T": "J",
        "U": "T",
        "V": "Q",
        "W": "E",
        "X": "G",
        "Y": "H",
        "Z": "Z"
}

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, mapping=MAPPING)
print(encrypted_message)
