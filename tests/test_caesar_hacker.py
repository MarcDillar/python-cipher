"""Unit Tests for the Caesar Cipher Hacker"""
import unittest
from .context import caesar, caesar_hacker

class CaesarCipherHackerTest(unittest.TestCase):
    """Unit Test Class"""

    def test_bruteforce(self):
        """Check if a message encrypted with a Caesar Cipher is found by brute force"""
        original_message = "This is my original message!"
        key = 13
        encrypted_message = caesar.CaesarCipher().encrypt(original_message, key)
        decrypted_messages = caesar_hacker.CaesarCipherHacker().brute_force(encrypted_message)

        message_found = original_message in decrypted_messages

        self.assertEqual(message_found, True)
