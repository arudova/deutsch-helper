import unittest
from custom_db import *


class TestCheck(unittest.TestCase):

    def setUp(self):
        sql = CustomDB()
        sql.open()
        self.data = sql.getDictionary()
        sql.close()

    def test_english_translation(self):
        word = 'Tochter'
        english_word = 'daughter'
        translated_word = [entry['english'] for entry in self.data
                           if entry['deutsch'] == word]
        self.assertEqual(english_word, translated_word[0])

    def test_deutsch_translation(self):
        word = 'daughter'
        deutsch_word = 'Tochter'
        translated_word = [entry['deutsch'] for entry in self.data
                           if entry['english'] == word]
        self.assertEqual(deutsch_word, translated_word[0])

    def test_cases(self):
        word = 'daughter'
        word_cases = 'die, die, der, der'
        cases = [(entry['nominativ'], entry['akkusativ'],
                 entry['dativ'], entry['genitiv']) for entry in self.data
                 if entry['english'] == word]
        self.assertEqual(word_cases, '%s, %s, %s, %s' % cases[0])

if __name__ == '__main__':
    unittest.main()
