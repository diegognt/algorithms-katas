"""
The palindrome word detector.

A palindrome words reasd the same backward as forward, like 'madam'. Devise an
algorithm that validates wheater a word of N characters is a palindrome.
"""
import unittest


def is_palindrome(word: str) -> bool:
    """Creates slice with negative step and confirm equality with word.

    Args:
        word (str): A string.

    Returns:
        True if the word is palindrome.
    """
    return word[::-1] == word


class PalindromeTestCase(unittest.TestCase):
    """Test if a word is a palindrome."""
    def test_madam_word(self):
        """Test is the 'madam' word is palindrome"""
        self.assertTrue(is_palindrome("madam"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
