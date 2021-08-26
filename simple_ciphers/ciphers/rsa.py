import random
from math import gcd
from .cipher import Cipher
from ..utils.math import generate_prime_number, modinv


class RSACipher(Cipher):
    '''
    Class handling basic RSA Cipher operations

    ...

    Methods
    -------
    encrypt(message, public_key):
        Encrypts a message

    decrypt(message, private_key):
        Decrypts a message
    '''

    def __init__(self):
        self.__generate_keys()

    def __generate_keys(self, keySize=1024):
        p, q = 0, 0

        # Create two prime numbers, p and q. Calculate n = p * q:
        while p == q:
            p = generate_prime_number(keySize)
            q = generate_prime_number(keySize)
        n = p * q

        # Create a number e that is relatively prime to (p-1)*(q-1):
        while True:
            e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
            if gcd(e, (p - 1) * (q - 1)) == 1:
                break

        # Calculate d, the mod inverse of e
        d = modinv(e, (p - 1) * (q - 1))

        self.publicKey = ",".join([keySize, n, e])
        self.privateKey = ",".join([keySize, n, d])
