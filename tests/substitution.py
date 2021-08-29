"""Unit Tests for the Simple Subsitution Cipher"""
import unittest
from .context import substitution, cipher_exceptions


class SimpleSubstitutionCipherTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "Here is the message that needs to be encrypted"
    MESSAGE_TO_DECRYPT = "Iaca sr jia narrlua jilj xaaor jp fa axwchbjao"
    KEY = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'

    def test_encrypt(self):
        """Test the result of an encryption"""
        cipher = substitution.SimpleSubstitutionCipher()

        encrypted_message = cipher.encrypt(
            self.MESSAGE_TO_ENCRYPT,
            key=self.KEY
        )
        self.assertEqual(encrypted_message, self.MESSAGE_TO_DECRYPT)

    def test_decrypt(self):
        """Test the result of a decryption"""
        cipher = substitution.SimpleSubstitutionCipher()

        decrypted_message = cipher.decrypt(
            self.MESSAGE_TO_DECRYPT,
            key=self.KEY
        )

        self.assertEqual(decrypted_message, self.MESSAGE_TO_ENCRYPT)

    def test_encrypt_method_incorrect_message(self):
        """
        Test that the encrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            substitution.SimpleSubstitutionCipher().encrypt(1, key=self.KEY)

    def test_encrypt_method_incorrect_key(self):
        """
        Test that the encrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            cipher = substitution.SimpleSubstitutionCipher()
            cipher.encrypt(self.MESSAGE_TO_ENCRYPT, key="a")

    def test_decrypt_method_incorrect_message(self):
        """
        Test that the decrypt method raises
        an Exception if the message is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectMessageError):
            substitution.SimpleSubstitutionCipher().decrypt(1, key=self.KEY)

    def test_decrypt_method_incorrect_key(self):
        """
        Test that the decrypt method raises
        an Exception if the key is incorrect
        """
        with self.assertRaises(cipher_exceptions.IncorrectCipherKeyError):
            cipher = substitution.SimpleSubstitutionCipher()
            cipher.decrypt(self.MESSAGE_TO_DECRYPT, key="a")

    def test_init_incorrect_symbols_list(self):
        """
        Test that the init method raises
        an Exception if the symbols argument is incorrect
        """
        with self.assertRaises(ValueError):
            substitution.SimpleSubstitutionCipher(simple=False, symbols=123)

    def test_cipher_incorrect_mode(self):
        """
        Test that the cipher method raises
        an Exception if the mode argument is incorrect
        """
        with self.assertRaises(ValueError):
            cipher = substitution.SimpleSubstitutionCipher()
            cipher.cipher("My message", key=2, mode="incorrect type")

    def test_reversible(self):
        """Test that an encrypted message can be decrypted with the same key"""

        cipher = substitution.SimpleSubstitutionCipher()

        message = cipher.encrypt(self.MESSAGE_TO_ENCRYPT, key=self.KEY)
        decrypted_message = cipher.decrypt(message, key=self.KEY)
        self.assertEqual(self.MESSAGE_TO_ENCRYPT, decrypted_message)


if __name__ == '__main__':
    unittest.main()
