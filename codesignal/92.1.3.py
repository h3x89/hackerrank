# https://learn.codesignal.com/course/92/unit/1/practice/3

# You are given a string filled with words. Your task is to write a Python function that takes this string as input. Your function should then capitalize the first letter of each word while making the rest of the letters lowercase. Finally, it should recombine the words into a new string where every word starts with a capital letter.

# Here's what to keep in mind:

# The input string will contain between 1 and 100 words.
# Each word is a sequence of characters separated by white space.
# Words consist of characters ranging from a to z, A to Z, 0 to 9, or even an underscore _.
# The provided string will not start or end with a space, and it will not contain double spaces.
# After capitalizing the first character of each word and converting the rest to lowercase, the program should return a single string in which the words maintain their original order.
# If the first character of a word is not a letter (like a number or an underscore), keep it as is.
# Ignore cases where punctuation marks are attached to words (such as "Hello," or "world!"). Words and punctuation should retain their original places in your final output. You are not required to separate punctuation marks from the words in your solution.

# Example

# For the input string "SoME rAndoM _TeXT", the output should be "Some Random _text".

def solution(input_str):
    # ok but not for all cases fe. "123 _hello"
    # return input_str.title() 

    # ok for all cases 
    # This solution works by:
    # 1. input_str.split() - splits the string into a list of words using whitespace as delimiter
    # 2. word.capitalize() - for each word:
    #    - If word starts with a letter, capitalizes first letter and lowercases rest
    #    - If word starts with non-letter (e.g. number/underscore), leaves it unchanged
    # 3. ' '.join() - joins the words back together with spaces between them
    return ' '.join(word.capitalize() for word in input_str.split())

# print(solution("SoME rAndoM _TeXT"))


import unittest

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("hello world"), 'Hello World')

    def test_2(self):
        self.assertEqual(solution("HELLO WORLD"), 'Hello World')

    def test_3(self):
        self.assertEqual(solution("123 hello"), '123 Hello')

    def test_4(self):
        self.assertEqual(solution("_underscore"), '_underscore')

    def test_5(self):
        self.assertEqual(
            solution("first second third fourth fifth sixth seventh eights ninth tenth"), 
            'First Second Third Fourth Fifth Sixth Seventh Eights Ninth Tenth'
        )

    def test_6(self):
        self.assertEqual(solution("single"), 'Single')

    def test_7(self):
        self.assertEqual(solution("Hello neat pythonistas_123"), 'Hello Neat Pythonistas_123')

    def test_8(self):
        self.assertEqual(solution("SoME rAndoM _TeXT"), 'Some Random _text')

    def test_9(self):
        self.assertEqual(solution("CAPS lock IS on"), 'Caps Lock Is On')

    def test_10(self):
        self.assertEqual(solution("mIxEd CaSe sample"), 'Mixed Case Sample')


if __name__ == '__main__':
    unittest.main()