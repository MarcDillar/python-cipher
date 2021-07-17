"""Unit Tests for the Simple Transposition Cipher"""
import unittest
from .context import transposition, cipher_exceptions


class SimpleTranspositionCipherTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "This is my original message!"
    MESSAGE_TO_DECRYPT = "Tiehg!iisn ails  mmeys soarg"
    KEY = 13

    def test_encrypt(self):
        """Test the result of an encryption"""
        cipher = transposition.SimpleTranspositionCipher()
        self.assertEqual(
            cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY),
            self.MESSAGE_TO_DECRYPT
        )

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = transposition.SimpleTranspositionCipher()

        self.assertEqual(
            cipher.decrypt(self.MESSAGE_TO_DECRYPT, self.KEY),
            self.MESSAGE_TO_ENCRYPT
        )

    def test_encrypt_method_incorrect_message(self):
        """
        Test that the encrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            transposition.SimpleTranspositionCipher().encrypt(1, 13)

    def test_encrypt_method_incorrect_key(self):
        """
        Test that the encrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(transposition.IncorrectCipherKeyError):
            cipher = transposition.SimpleTranspositionCipher()
            cipher.encrypt("This is another message", "a")

    def test_decrypt_method_incorrect_message(self):
        """
        Test that the decrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(transposition.IncorrectMessageError):
            transposition.SimpleTranspositionCipher().decrypt(1, 13)

    def test_decrypt_method_incorrect_key(self):
        """
        Test that the decrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            cipher = transposition.SimpleTranspositionCipher()
            cipher.decrypt("This is another message", "a")

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same key"""
        message = "this is a message 1234"
        key = 11
        cipher = transposition.SimpleTranspositionCipher()
        encrypted_message = cipher.encrypt(message, key)
        decrypted_message = cipher.decrypt(encrypted_message, key)
        self.assertEqual(message, decrypted_message)


if __name__ == '__main__':
    unittest.main()
