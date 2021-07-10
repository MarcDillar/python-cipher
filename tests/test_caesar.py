"""Unit Tests for Caesar Cipher"""
import unittest
from .context import ciphers

class CaesarCipherTest(unittest.TestCase):
    """Unit Test Class"""

    def test_encrypt(self):
        """Test the result of an encryption"""
        cipher = ciphers.caesar.CaesarCipher()
        encrypted_message = cipher.encrypt("This is my original message!", 13)
        self.assertEqual(encrypted_message, "'uvF7vF7zL7BEvtvAny7zrFFntr.")

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = ciphers.caesar.CaesarCipher()
        decrypted_message = cipher.decrypt("'uvF7vF7zL7BEvtvAny7zrFFntr.", 13)
        self.assertEqual(decrypted_message, "This is my original message!")

    def test_encrypt_method_incorrect_message(self):
        """Test that the encrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(ciphers.exceptions.IncorrectMessageError):
            ciphers.caesar.CaesarCipher().encrypt(1, 13)

    def test_encrypt_method_incorrect_key(self):
        """Test that the encrypt method raises an Exception if the key is incorrect"""
        with self.assertRaises(ciphers.exceptions.IncorrectCipherKeyError):
            ciphers.caesar.CaesarCipher().encrypt("This is another message", "a")

    def test_decrypt_method_incorrect_message(self):
        """Test that the decrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(ciphers.exceptions.IncorrectMessageError):
            ciphers.caesar.CaesarCipher().decrypt(1, 13)

    def test_decrypt_method_incorrect_key(self):
        """Test that the decrypt method raises an Exception if the key is incorrect"""
        with self.assertRaises(ciphers.exceptions.IncorrectCipherKeyError):
            ciphers.caesar.CaesarCipher().decrypt("This is another message", "a")

    def test_init_incorrect_symbols_list(self):
        """Test that the init method raises an Exception if the symbols argument is incorrect"""
        with self.assertRaises(ValueError):
            ciphers.caesar.CaesarCipher(symbols=123)

    def test_cipher_incorrect_mode(self):
        """Test that the cipher method raises an Exception if the mode argument is incorrect"""
        with self.assertRaises(ValueError):
            ciphers.caesar.CaesarCipher().cipher("My message", 2, mode="incorrect cipher type")

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same key"""
        message = "this is a message 1234"
        key = 12

        encrypted_message = ciphers.caesar.CaesarCipher().encrypt(message, key)
        decrypted_message = ciphers.caesar.CaesarCipher().decrypt(encrypted_message, key)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
