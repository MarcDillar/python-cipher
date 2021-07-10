"""Unit Tests for the Caesar Cipher Hacker"""
import unittest
from .context import ciphers, hackers

class CaesarCipherHackerTest(unittest.TestCase):
    """Unit Test Class"""

    def test_bruteforce(self):
        """Check if a message encrypted with a Caesar Cipher is found by brute force"""
        original_message = "This is my original message!"
        key = 13
        encrypted_message = ciphers.caesar.CaesarCipher().encrypt(original_message, key)
        decrypted_messages = hackers.caesar.CaesarCipherHacker().brute_force(encrypted_message)

        message_found = original_message in decrypted_messages

        self.assertEqual(message_found, True)
