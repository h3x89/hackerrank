# https://learn.codesignal.com/course/93/unit/2/practice/1

# n this task, we are manipulating sentences and strings using nested loops. You will be given a string representing a sentence where words are separated by spaces. Your objective is to write a Python function that selects the even-indexed characters of words containing an odd number of characters.

# This sentence string will have a maximum length of 500 characters, including spaces.

# Subsequently, these characters must be combined into a single string in the order they appear in the sentence, but the final output string will be reversed end-to-end.

# For instance, if the input sentence is "Coding tasks are fun and required", the output string should be "tssaefnad", which, when reversed, becomes "danfeasst". The words "tasks", "are", "fun", and "and" are selected since they have an odd number of characters, and the characters 't', 's', 's', 'a', 'e', 'f', 'n', 'a', 'd' at even indexes are chosen and then reversed in the final string. Do not forget that Python indexing begins at 0, so 't' in "tasks" is considered to be at an even index. Single-character words must also be taken into consideration for this task.

# Are you ready to accept the challenge and create a solution that efficiently accomplishes this task step by step?

def solution(sentence):
    result = []
    for word in sentence.split():
        if len(word) % 2 == 1:
            for i in range(0, len(word), 2):
                result.append(word[i])
    return ''.join(result)[::-1]

print(solution("Coding tasks are fun and required")) # "danfeasst"

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("Coding tasks are fun and required"), "danfeasst")

    def test2(self):
        self.assertEqual(solution("etrnal"), "")

    def test3(self):
        self.assertEqual(solution("awe-inspiring"), "giisiea")

    def test4(self):
        self.assertEqual(solution("a a"), "aa")

    def test5(self):
        self.assertEqual(solution("python coding"), "")

    def test6(self):
        self.assertEqual(solution("Hello, world!"), "")

    def test7(self):
        self.assertEqual(solution("Mastering Advanced Looping and Implementation"), "dagioLgiesM")

    def test8(self):
        self.assertEqual(solution("Stay hungry, Stay foolish."), ",rnh")

    def test9(self):
        self.assertEqual(solution("! o G e h C o s i M P"), "PMisoCheGo!")

    def test10(self):
        self.assertEqual(solution("abcdefghijklmnopqrstuvwxyz"), "")

if __name__ == '__main__':
    unittest.main()