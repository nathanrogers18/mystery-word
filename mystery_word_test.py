import unittest


from mystery_word import *


class TestGetWordList(unittest.TestCase):
    # NEED SOME HELP HERE
    pass


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
    pass


class TestGetNormalWords(unittest.TestCase):
    pass


class TestGetHardWords(unittest.TestCase):
    pass


class TestGetRandomWord(unittest.TestCase):
    pass


class TestDisplayWord(unittest.TestCase):
    pass

class TestWordGuessed(unittest.TestCase):
    pass

class TestGetAnswer(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()
