import unittest
from evil_mystery_word import *

#COPIED FROM ORIGINAL, CHANGE THIS FOR EVIL
class TestCreateWordFamilies(unittest.TestCase):
    def test_create_word_families(self):
        test_word_list = ['echo', 'heal', 'best', 'lazy']
        test_guessed_letter_list = ['e']
        word_families = create_word_families(4, test_word_list,
                                             test_guessed_letter_list)
        expected_word_families = {'e---': ['echo'],
                                  '-e--': ['heal', 'best'],
                                  '----': ['lazy']}
        self.assertTrue(word_families == expected_word_families) # CHECK TO SEE IF THIS ACTUALLY WILL WORK




if __name__ == '__main__':
    unittest.main()
