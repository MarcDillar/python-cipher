""" Cipher Exception classes """

class IncorrectCipherKeyError(ValueError):
    """Error raised if the cipher key is incorrect"""
    def __init__(self):
        super().__init__("The cipher key has to be an integer")

class IncorrectMessageError(ValueError):
    """Error raised if the message to encrypt/decrypt is incorrect"""
    def __init__(self):
        super().__init__("The message to be encrypted has to be a string!")
