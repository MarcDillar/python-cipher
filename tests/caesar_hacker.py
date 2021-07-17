"""Unit Tests for the Caesar Cipher Hacker"""
import unittest
from .context import caesar, caesar_hacker


class CaesarCipherHackerTest(unittest.TestCase):
    """Unit Test Class"""

    MESSAGE_TO_ENCRYPT = "This is my original message!"
    KEY = 13

    def test_bruteforce(self):
        """
        Check if a message encrypted with
        a Caesar Cipher is found by brute force
        """
        cipher = caesar.CaesarCipher()
        encrypted_message = cipher.encrypt(
            self.MESSAGE_TO_ENCRYPT,
            self.KEY
        )

        hacker = caesar_hacker.CaesarCipherHacker()
        decrypted_messages = hacker.brute_force(encrypted_message)

        message_found = self.MESSAGE_TO_ENCRYPT in decrypted_messages

        self.assertEqual(message_found, True)
