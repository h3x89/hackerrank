# https://learn.codesignal.com/course/92/unit/2/practice/2

# You are given a string s of length n, with n ranging from 1 to 500 inclusive. This string represents the complex and jumbled record of a sports game. It combines player names and scores but lacks a uniform structure. The player names consist of words made up of lowercase English alphabets (a-z), while the scores are integers ranging from 1 to 100 inclusive.

# Your mission involves writing a Python function solution(). This function should parse the given string, isolate the integers representing player scores, and return the sum of these scores.

# For instance, for the input string, "joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe", your function should return the sum 5 + 10 + 2 + 1, which totals 18.

def solution(s):
    # split the string into a list of words
    words = s.split()
    sum = 0
    # iterate over the list of words
    for i in range(len(words)):
        # if the word is a number, add it to the sum
        word = words[i]
        
        #remove the comma and the word
        # word = word.replace(",", "")
       
        # remove from word all non-digit characters
        word = ''.join(char for char in word if char.isdigit())
        if word.isdigit():
            sum += int(word)
    return sum

# print(solution("joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"))   
print(solution(" 10 scored 2, with an extra 1 point scored by joe"))   

import unittest

class SolutionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution("joe scored 5 points, while adam scored 10 points and bob scored 2, with an extra 1 point scored by joe"), 18)
        
    def test_2(self):
        self.assertEqual(solution("michael scored 100 points"), 100)
        
    def test_3(self):
        self.assertEqual(solution("lena scored 50 points and lee scored 50 points"), 100)
        
    def test_4(self):
        self.assertEqual(solution("sam scored 25 points, john scored 25 points, jim scored 25 points, and sue scored 25 points"), 100)
        
    def test_5(self):
        self.assertEqual(solution("1 point scored by max"), 1)
        
    def test_6(self):
        self.assertEqual(solution("no points scored in this game"), 0)
        
    def test_7(self):
        self.assertEqual(solution("abc scored 3 points and def scored 9 points then ghi scored 27 points"), 39)
        
    def test_8(self):
        self.assertEqual(solution("game score: pete 2 points, eve 4 points, zane 8 points"), 14)
        
    def test_9(self):
        self.assertEqual(solution("jake scored1point, john scored2points"), 3)
        
    def test_10(self):
        self.assertEqual(solution("this game ended with no score"), 0)


if __name__ == '__main__':
    unittest.main()