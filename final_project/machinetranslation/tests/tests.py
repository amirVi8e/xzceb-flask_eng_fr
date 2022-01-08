import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('I am Amir'), 'Je suis Amir')
        self.assertEqual(english_to_french('Nice to meet you'), 'Ravi de vous rencontrer')

    def test2(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Je m\'appelle Amir'), 'My name is Amir')
        self.assertEqual(french_to_english('Et toi?'), 'And you?')

    def test2(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()