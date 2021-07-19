"""Example of message decryption using the Simple Substitution cipher"""

from simple_ciphers.ciphers.substitution import SimpleSubstitutionCipher

MESSAGE_TO_DECRYPT = "Iaca sr jia narrlua jilj xaaor jp fa axwchbjao"

cipher = SimpleSubstitutionCipher()

# Decryption with a key
KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
decrypted_message = cipher.decrypt(message=MESSAGE_TO_DECRYPT, key=KEY)
print(decrypted_message)

# Decryption with a mapping dictionnary
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

decrypted_message = cipher.decrypt(message=MESSAGE_TO_DECRYPT, mapping=MAPPING)
print(decrypted_message)
