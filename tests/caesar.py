"""Unit Tests for the Caesar Cipher"""
import unittest
from .context import caesar, cipher_exceptions


class CaesarCipherTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "This is my original message!"
    MESSAGE_TO_DECRYPT = "'uvF7vF7zL7BEvtvAny7zrFFntr."
    KEY = 13

    def test_encrypt(self):
        """Test the result of an encryption"""
        cipher = caesar.CaesarCipher()
        encrypted_message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY)
        self.assertEqual(encrypted_message, self.MESSAGE_TO_DECRYPT)

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = caesar.CaesarCipher()
        decrypted_message = cipher.decrypt("'uvF7vF7zL7BEvtvAny7zrFFntr.", 13)
        self.assertEqual(decrypted_message, "This is my original message!")

    def test_encrypt_method_incorrect_message(self):
        """
        Test that the encrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            caesar.CaesarCipher().encrypt(1, 13)

    def test_encrypt_method_incorrect_key(self):
        """
        Test that the encrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            caesar.CaesarCipher().encrypt("This is another message", "a")

    def test_decrypt_method_incorrect_message(self):
        """
        Test that the decrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            caesar.CaesarCipher().decrypt(1, 13)

    def test_decrypt_method_incorrect_key(self):
        """
        Test that the decrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            caesar.CaesarCipher().decrypt("This is another message", "a")

    def test_init_incorrect_symbols_list(self):
        """
        Test that the init method raises
        an Exception if the symbols argument is incorrect
        """
        with self.assertRaises(ValueError):
            caesar.CaesarCipher(symbols=123)

    def test_cipher_incorrect_mode(self):
        """
        Test that the cipher method raises
        an Exception if the mode argument is incorrect
        """
        with self.assertRaises(ValueError):
            cipher = caesar.CaesarCipher()
            cipher.cipher("My message", 2, mode="incorrect cipher type")

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same key"""
        cipher = caesar.CaesarCipher()

        encrypted_message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY)
        decrypted_message = cipher.decrypt(encrypted_message, self.KEY)
        self.assertEqual(encrypted_message, decrypted_message)


if __name__ == '__main__':
    unittest.main()
