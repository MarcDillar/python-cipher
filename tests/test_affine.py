"""Unit Tests for the Caesar Cipher"""
import unittest
from .context import affine, cipher_exceptions

class AffineCipherTest(unittest.TestCase):
    """Unit Test Class"""

    def test_encrypt(self):
        """Test the result of an encryption"""

        MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
        KEY_A = 7
        KEY_B = 47

        cipher = affine.AffineCipher()

        encrypted_message = cipher.encrypt(MESSAGE_TO_ENCRYPT, KEY_A, KEY_B)
        self.assertEqual(encrypted_message, "w%,H5,H5O%J51JHHhXJ5O%hO5*,  5oJ5J8vA\mOJC")

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = affine.AffineCipher()

        MESSAGE_TO_DECRYPT = "w%,H5,H5O%J51JHHhXJ5O%hO5*,  5oJ5J8vA\mOJC"
        KEY_A = 7
        KEY_B = 47

        decrypted_message = cipher.decrypt(MESSAGE_TO_DECRYPT, KEY_A, KEY_B)
        self.assertEqual(decrypted_message, "This is the message that will be encrypted")

    def test_encrypt_method_incorrect_message(self):
        """Test that the encrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            affine.AffineCipher().encrypt(1, 13, 20)

    def test_encrypt_method_key_a_NaN(self):
        """Test that the encrypt method raises an Exception if key A is not an integer"""
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().encrypt("This is another message", "a", 2)

    def test_encrypt_method_key_b_NaN(self):
        """Test that the encrypt method raises an Exception if key B is not an integer"""
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().encrypt("This is another message", 2, "a")

    def test_encrypt_method_invalid_key_a(self):
        """
            Test that the encrypt method raises an Exception if key A is not relatively prime
            to the symbols set length
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher(symbols="ABCD").encrypt("This is another message", 4, 10)

    def test_decrypt_method_incorrect_message(self):
        """Test that the decrypt method raises an Exception if the message is incorrect"""
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            affine.AffineCipher().decrypt(1, 13, 20)

    def test_decrypt_method_key_a_NaN(self):
        """Test that the decrypt method raises an Exception if key A is not an integer"""
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().decrypt("This is another message", "a", 2)

    def test_decrypt_method_key_b_NaN(self):
        """Test that the decrypt method raises an Exception if key B is not an integer"""
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().decrypt("This is another message", 2, "a")

    def test_decrypt_method_invalid_key_a(self):
        """
            Test that the decrypt method raises an Exception if key A is not relatively prime
            to the symbols set length
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher(symbols="ABCD").decrypt("This is another message", 4, 10)

    def test_init_incorrect_symbols_list(self):
        """Test that the init method raises an Exception if the symbols argument is incorrect"""
        with self.assertRaises(ValueError):
            affine.AffineCipher(symbols=123)

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same keys"""
        MESSAGE = "this is a message 1234"
        KEY_A = 13
        KEY_B = 20

        encrypted_message = affine.AffineCipher().encrypt(MESSAGE, KEY_A, KEY_B)
        decrypted_message = affine.AffineCipher().decrypt(encrypted_message, KEY_A, KEY_B)
        self.assertEqual(MESSAGE, decrypted_message)

if __name__ == '__main__':
    unittest.main()
