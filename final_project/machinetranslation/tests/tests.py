"""modules"""
import unittest
from translator import english_to_french
from translator import french_to_english
class TestTranslator(unittest.TestCase):
    """tests for the Translator module"""
    def test_null(self):
        """tests if functions return None"""
        etf = english_to_french('Hello')
        fte = french_to_english('Bonjour')
        null = None
        etf_null_error = "english_to_french returns None"
        fte_null_error = "french_to_english returns None"
        self.assertNotEqual(etf, null, etf_null_error)
        self.assertNotEqual(fte, null, fte_null_error)
    def test_working(self):
        """tests if functions return correct tramslations"""
        etf = english_to_french('Hello')
        fte = french_to_english('Bonjour')
        ehello = "Hello"
        fhello = "Bonjour"
        etf_broke_message = "english_to_french not working correctly"
        fte_broke_message = "french_to_english not working correctly"
        self.assertEqual(etf, fhello, etf_broke_message)
        self.assertEqual(fte, ehello, fte_broke_message)

if __name__ == '__main__':
    unittest.main()
