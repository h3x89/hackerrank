# https://learn.codesignal.com/course/93/unit/2/practice/3

# You are given a string that represents a sentence in which words are separated by spaces. Your task is to create a Python function that identifies and concatenates the second half of each word with an even number of characters, ensuring the characters of this second half go before the character c in the ASCII table. Then, combine these characters into a single string, maintaining the order in which they appear in the sentence.

# The input sentence consists of ASCII characters from the space character (' ') up to the tilde character ('~'), with its length ranging between 1 and 500, inclusive. These characters form words separated by spaces, without any consecutive space characters.

# For example, consider the sentence: "Python is a high-level programming language." and the character "n". The word 'Python' consists of 6 characters (an even number), and the second half of this word is 'hon'. In this second half, only 'h' is less than 'n'.

# The output of your function, in this case, should be: "h", as it's the only character that meets the conditions.

# For the character comparison ('<' character), use the ASCII values since all characters in the sentence are ASCII. ASCII codes for characters can be found by using Python's built-in function ord().

def solution(sentence, c):
    result = []
    for word in sentence.split():
        if len(word) % 2 == 0:
            second_half = word[len(word)//2:]
            for char in second_half:
                if char < c:
                    result.append(char)
    return ''.join(result)

print(solution("Python is a high-level programming language.", "n")) # "h"

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solution("Python is a high-level programming language.", 'n'), 
            "hleel"
        )

    def test2(self):
        self.assertEqual(
            solution("Practice makes perfect.", 'f'), 
            "ceec."
        )

    def test3(self):
        self.assertEqual(
            solution("Mastering Advanced Looping and Implementation.", 'l'), 
            "ced"
        )

    def test4(self):
        self.assertEqual(
            solution("I will pass this test!", 'w'), 
            "llssis"
        )

    def test5(self):
        self.assertEqual(
            solution("Participate in exciting challenges.", 'a'), 
            ""
        )

    def test6(self):
        self.assertEqual(
            solution("The quick brown fox jumps over the lazy dog.", 'f'), 
            "e."
        )

    def test7(self):
        self.assertEqual(
            solution("This sentence is a test sentence.", 't'), 
            "isencess"
        )

    def test8(self):
        self.assertEqual(
            solution("This is a long string with lots of characters and words.", 'v'), 
            "issngingthtsfctersds."
        )

    def test9(self):
        self.assertEqual(
            solution("Another sentence to test the function.", 'o'), 
            "ence"
        )

    def test10(self):
        self.assertEqual(
            solution("Some additional variety in test cases.", 'k'), 
            "eiae."
        )

if __name__ == '__main__':
    unittest.main()