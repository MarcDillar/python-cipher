"""Unit Tests for the Caesar Cipher"""
import unittest
from .context import affine, cipher_exceptions


class AffineCipherTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
    MESSAGE_TO_DECRYPT = "w%,H5,H5O%J51JHHhXJ5O%hO5*,  5oJ5J8vA\mOJC"
    MESSAGE_TO_DECRYPT_SIMPLE = "YSZr Zr ySx BxrrVLx ySVy TZuu cx xIjkhWyxq"
    KEY_A = 7
    KEY_B = 47

    def test_encrypt(self):
        """Test the result of an encryption"""

        cipher = affine.AffineCipher(simple=False)

        encrypted_message = cipher.encrypt(
            self.MESSAGE_TO_ENCRYPT,
            self.KEY_A,
            self.KEY_B
        )
        self.assertEqual(encrypted_message, self.MESSAGE_TO_DECRYPT)

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = affine.AffineCipher(simple=False)
        decrypted_message = cipher.decrypt(
            self.MESSAGE_TO_DECRYPT,
            self.KEY_A,
            self.KEY_B
        )
        self.assertEqual(decrypted_message, self.MESSAGE_TO_ENCRYPT)

    def test_encrypt_method_incorrect_message(self):
        """
        Test that the encrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            affine.AffineCipher().encrypt(1, 13, 20)

    def test_encrypt_method_key_a_NaN(self):
        """
        Test that the encrypt method raises
        an Exception if key A is not an integer
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().encrypt("This is another message", "a", 2)

    def test_encrypt_method_key_b_NaN(self):
        """
        Test that the encrypt method raises
        an Exception if key B is not an integer
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().encrypt("This is another message", 2, "a")

    def test_encrypt_method_invalid_key_a(self):
        """
            Test that the encrypt method raises
            an Exception if key A is not relatively prime
            to the symbols set length
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            cipher = affine.AffineCipher(symbols="ABCD")
            cipher.encrypt("This is another message", 4, 10)

    def test_decrypt_method_incorrect_message(self):
        """
        Test that the decrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            affine.AffineCipher().decrypt(1, 13, 20)

    def test_decrypt_method_key_a_NaN(self):
        """
        Test that the decrypt method raises
        an Exception if key A is not an integer
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().decrypt("This is another message", "a", 2)

    def test_decrypt_method_key_b_NaN(self):
        """
        Test that the decrypt method raises
        an Exception if key B is not an integer
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            affine.AffineCipher().decrypt("This is another message", 2, "a")

    def test_decrypt_method_invalid_key_a(self):
        """
            Test that the decrypt method raises
            an Exception if key A is not relatively prime
            to the symbols set length
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            cipher = affine.AffineCipher(symbols="ABCD")
            cipher.decrypt("This is another message", 4, 10)

    def test_init_incorrect_symbols_list(self):
        """
        Test that the init method raises
        an Exception if the symbols argument is incorrect
        """
        with self.assertRaises(ValueError):
            affine.AffineCipher(simple=False, symbols=123)

    def test_reversible(self):
        """Test that an encrypted message can be derypted with the same keys"""

        cipher = affine.AffineCipher()
        encrypted_message = cipher.encrypt(
            self.MESSAGE_TO_ENCRYPT,
            self.KEY_A,
            self.KEY_B
        )
        decrypted_message = cipher.decrypt(
            encrypted_message,
            self.KEY_A,
            self.KEY_B
        )
        self.assertEqual(self.MESSAGE_TO_ENCRYPT, decrypted_message)


if __name__ == '__main__':
    unittest.main()
