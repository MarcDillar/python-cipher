"""Unit Tests for the Simple Transposition Cipher"""
import unittest
from .context import transposition, cipher_exceptions

class SimpleTranspositionCipherTest(unittest.TestCase):
    """Unit Test Class"""

    def test_encrypt(self):
        """Test the result of an encryption"""
        self.assertEqual(transposition.SimpleTranspositionCipher().encrypt("This is my original message!", 13), "Tiehg!iisn ails  mmeys soarg")

    def test_decrypt(self):
        """Test the result of a decryption"""
        self.assertEqual(transposition.SimpleTranspositionCipher().decrypt("Tiehg!iisn ails  mmeys soarg", 13), "This is my original message!")

    def test_encrypt_method_incorrect_message(self):
        """Test that the encrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            transposition.SimpleTranspositionCipher().encrypt(1, 13)

    def test_encrypt_method_incorrect_key(self):
        """Test that the encrypt method raises an Exception if the key is incorrect"""
        with self.assertRaises(transposition.IncorrectCipherKeyError):
            transposition.SimpleTranspositionCipher().encrypt("This is another message", "a")

    def test_decrypt_method_incorrect_message(self):
        """Test that the decrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(transposition.IncorrectMessageError):
            transposition.SimpleTranspositionCipher().decrypt(1, 13)

    def test_decrypt_method_incorrect_key(self):
        """Test that the decrypt method raises an Exception if the key is incorrect"""
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            transposition.SimpleTranspositionCipher().decrypt("This is another message", "a")

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same key"""
        message = "this is a message 1234"
        key = 11

        encrypted_message = transposition.SimpleTranspositionCipher().encrypt(message, key)
        decrypted_message = transposition.SimpleTranspositionCipher().decrypt(encrypted_message, key)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
