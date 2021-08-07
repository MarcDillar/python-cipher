"""Unit Tests for the Vigenere Cipher"""
import unittest
from .context import vigenere, cipher_exceptions


class VigenereCipherTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "Here is the message that will be encrypted."
    MESSAGE_TO_DECRYPT = "Alzw ia lhq keuapni khkx ubst te mfcdwpvms."
    KEY = "This is my cipher key"

    def test_encrypt_simple(self):
        """Test the result of an encryption using the simple mode"""
        cipher = vigenere.VigenereCipher()
        encrypted_message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY)
        self.assertEqual(
            encrypted_message,
            self.MESSAGE_TO_DECRYPT
        )

    def test_decrypt_simple(self):
        """Test the result of a decryption using the simple mode"""
        cipher = vigenere.VigenereCipher()
        decrypted_message = cipher.decrypt(
            self.MESSAGE_TO_DECRYPT,
            self.KEY
        )
        self.assertEqual(decrypted_message, self.MESSAGE_TO_ENCRYPT)

    def test_encrypt_method_incorrect_message(self):
        """
        Test that the encrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            vigenere.VigenereCipher().encrypt(1, self.KEY)

    def test_encrypt_method_incorrect_key(self):
        """
        Test that the encrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            vigenere.VigenereCipher().encrypt("This is another message", 1)

    def test_decrypt_method_incorrect_message(self):
        """
        Test that the decrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            vigenere.VigenereCipher().decrypt(1, self.KEY)

    def test_decrypt_method_incorrect_key(self):
        """
        Test that the decrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            vigenere.VigenereCipher().decrypt("This is another message", 1)

    def test_init_incorrect_symbols_list(self):
        """
        Test that the init method raises
        an Exception if the symbols argument is incorrect
        """
        with self.assertRaises(ValueError):
            vigenere.VigenereCipher(simple=False, symbols=123)

    def test_cipher_incorrect_mode(self):
        """
        Test that the cipher method raises
        an Exception if the mode argument is incorrect
        """
        with self.assertRaises(ValueError):
            cipher = vigenere.VigenereCipher()
            cipher.cipher("My message", self.KEY, mode="incorrect cipher type")

    def test_reversible_simple(self):
        """
        Test that an encrypted message can be decrypted
        with the same key using the simple mode
        """
        cipher = vigenere.VigenereCipher()

        encrypted_message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY)
        decrypted_message = cipher.decrypt(encrypted_message, self.KEY)
        self.assertEqual(self.MESSAGE_TO_ENCRYPT, decrypted_message)

    def test_reversible(self):
        """
        Test that an encrypted message can be decrypted
        with the same key
        """
        cipher = vigenere.VigenereCipher()

        encrypted_message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, self.KEY)
        decrypted_message = cipher.decrypt(encrypted_message, self.KEY)
        self.assertEqual(self.MESSAGE_TO_ENCRYPT, decrypted_message)


if __name__ == '__main__':
    unittest.main()
