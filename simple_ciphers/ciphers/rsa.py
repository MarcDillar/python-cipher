import random
from string import printable
from math import gcd, log
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

    def __init__(self, simple=True, symbols=printable):
        super().__init__(simple=simple)
        self.symbols = symbols
        self.__generate_keys()

    def __get_maximum_block_size(self):
        self.maximum_block_size = log(2 ** self.keySize, len(self.symbols))

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

        self.keySize = keySize
        self.publicKey = (n, e)
        self.privateKey = (n, d)
        self.__get_maximum_block_size()

    def __get_blocks_from_text(self, message, blockSize):
        for character in message:
            if character not in self.symbols:
                raise ValueError(
                    f"Character {character} doesn't exist in the symbol set."
                    )

        blocks = []

        for blockStart in range(0, len(message), blockSize):
            blockInt = 0
            blockEnd = min(blockStart + blockSize, len(message))

            for i in range(blockStart, blockEnd):
                char_val = (self.symbols.index(message[i]))
                offset = (len(self.symbols) ** (i % blockSize))
                blockInt += char_val * offset
            blocks.append(blockInt)

        return blocks

    def __get_text_from_blocks(self, blocks, message_length, blockSize):
        message = []
        for blockInt in blocks:
            blockMessage = []
            for i in range(blockSize - 1, -1, -1):
                if len(message) + i < message_length:
                    charIndex = blockInt // (len(self.symbols) ** i)
                    blockInt = blockInt % (len(self.symbols) ** i)
                    blockMessage.insert(0, self.symbols[charIndex])
            message.extend(blockMessage)
        return ''.join(message)

    def encrypt(self, message, blockSize=None):

        if not blockSize:
            blockSize = int(self.maximum_block_size)

        if self.maximum_block_size < blockSize:
            raise ValueError('Block size is too large')

        encryptedBlocks = []
        n, e = self.publicKey

        blocks = self.__get_blocks_from_text(message, blockSize)

        for block in blocks:
            encryptedBlocks.append(pow(block, e, n))

        return len(message), blockSize, encryptedBlocks

    def decrypt(self, message_length, blockSize, encryptedBlocks):
        if self.maximum_block_size < blockSize:
            raise ValueError('Block size is too large')

        decryptedBlocks = []
        n, d = self.privateKey
        for block in encryptedBlocks:
            decryptedBlocks.append(pow(block, d, n))

        return self.__get_text_from_blocks(
            decryptedBlocks,
            message_length,
            blockSize
        )
