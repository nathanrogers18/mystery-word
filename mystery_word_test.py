import unittest
from mystery_word import *


class TestGetWordList(unittest.TestCase):
    def test_list_created(self):
        test_word_list = get_word_list()
        self.assertTrue(len(test_word_list) > 0 and
                        isinstance(test_word_list, list))

class TestIsEasyWord(unittest.TestCase):
    def test_too_small(self):
        self.assertFalse(is_easy_word('cat'))
    def test_too_big(self):
        self.assertFalse(is_easy_word('monkeys'))
    def test_just_right(self):
        self.assertTrue(is_easy_word('dogs'))


class TestIsNormalWord(unittest.TestCase):
    def test_too_small(self):
        self.assertFalse(is_normal_word('doggy'))
    def test_too_big(self):
        self.assertFalse(is_normal_word('dalmations'))
    def test_just_right(self):
        self.assertTrue(is_normal_word('doggies'))


class TestIsHardWord(unittest.TestCase):
    def test_too_small(self):
        self.assertFalse(is_hard_word('doggy'))
    def test_just_right(self):
        self.assertTrue(is_hard_word('dalmations'))


class TestGetEasyWords(unittest.TestCase):
    def test_get_correct_words(self):
        test_word_list = ['anteater', 'cat', 'dalmations', 'doggies', 'doggy',
                          'dogs', 'monkey', 'orangutans']
        expected_easy_words = ['doggy', 'dogs', 'monkey']
        self.assertTrue(get_easy_words(test_word_list) == expected_easy_words)


class TestGetNormalWords(unittest.TestCase):
    def test_get_correct_words(self):
        test_word_list = ['anteater', 'cat', 'dalmations', 'doggies', 'doggy',
                          'dogs', 'monkey', 'orangutans']
        expected_normal_words = ['anteater', 'doggies', 'monkey']
        self.assertTrue(get_normal_words(test_word_list) == expected_normal_words)

class TestGetHardWords(unittest.TestCase):
    def test_get_correct_words(self):
        test_word_list = ['anteater', 'cat', 'dalmations', 'doggies', 'doggy',
                          'dogs', 'monkey', 'orangutans']
        expected_hard_words = ['dalmations', 'orangutans']
        self.assertTrue(get_hard_words(test_word_list) == expected_hard_words)


class TestGetRandomWord(unittest.TestCase):
    def test_word_in_list(self):
        test_word_list = ['anteater', 'cat', 'dalmations', 'doggies', 'doggy',
                          'dogs', 'monkey', 'orangutans']
        self.assertTrue(get_random_word(test_word_list) in test_word_list)


class TestDisplayWord(unittest.TestCase):
    def display_partial_word(self):
        test_answer = 'orangutans'
        test_guessed_letter_list = ['o', 'a', 'g', 'n']
        expected_display = 'o _ a _ n g _ _ a n _ '
        self.assertTrue(display_word(test_answer, test_guessed_letter_list) ==
                        expected_display)


class TestWordGuessed(unittest.TestCase):
    def test_not_guessed(self):
        test_answer = 'orangutans'
        test_guessed_letter_list = ['o', 'a', 'g', 'n']
        self.assertFalse(word_guessed(test_answer, test_guessed_letter_list))

    def test_guessed(self):
        test_answer = 'orangutans'
        test_guessed_letter_list = ['o', 'r', 'a', 'n', 'g', 'u', 't', 's']
        self.assertTrue(word_guessed(test_answer, test_guessed_letter_list))


class TestGetAnswer(unittest.TestCase):
    """
    QUESTIONS:
    1. Not sure how I'd simulate the user inputs, or if testing necessary
    2. Should function get_answer just be part of main()?
    """
    pass



if __name__ == '__main__':
    unittest.main()
