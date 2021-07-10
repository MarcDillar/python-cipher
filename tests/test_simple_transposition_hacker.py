"""Unit Tests for the Simple Transposition Cipher Hacker Cipher"""
import unittest
from .context import ciphers, hackers

class SimpleTranspositionCipherHackerTest(unittest.TestCase):
    """Unit Test Class"""

    def test_bruteforce(self):
        """Check if a message encrypted with a
        Simple Transposition Cipher is found by brute force"""

        original_message = "This is my original message! The message contains several sentences"
        key = 20

        cipher = ciphers.transposition.SimpleTranspositionCipher()
        hacker = hackers.transposition.SimpleTranspositionCipherHacker()

        encrypted_message = cipher.encrypt(original_message, key)
        decrypted_messages = hacker.brute_force(encrypted_message)

        message_found = original_message in decrypted_messages

        self.assertEqual(message_found, True)
