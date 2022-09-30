import unittest
from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def englishTest(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french(''), 'Bonjour')

class test_french_to_english(unittest.TestCase):
    def frenchTest(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english(''), 'Hello')

unittest.main()