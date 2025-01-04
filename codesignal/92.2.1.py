# https://learn.codesignal.com/course/92/unit/2/practice/1

# Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should convert to 'a', and 'a' should convert to '1'.

# You need to return a new string with the converted words, rejoined with hyphens.

# Ensure you maintain the original order of the words from the input string in your output string.

# The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.

# Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

# Example

# For the input string "1-a-3-c-5", the output should be "a-1-c-3-e".

def solution(word):
    # split the word into a list of words
    word_list = word.split("-")

    # iterate over the list of words
    for i in range(len(word_list)):
        # if the word is a number, convert it to a letter
        if word_list[i].isdigit():
            word_list[i] = chr(int(word_list[i]) + 96)
        # if the word is a letter, convert it to a number
        else:
            word_list[i] = str(ord(word_list[i]) - 96)
    # join the list of words back into a string
    return "-".join(word_list)

print(solution("1-a-3-c-5"))

import unittest

class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution("1-2-3-4-5"), "a-b-c-d-e")

    def test2(self):
        self.assertEqual(solution("a-b-c"), "1-2-3")
        
    def test3(self):
        self.assertEqual(solution("1-a-3-c-5"), "a-1-c-3-e")
        
    def test4(self):
        self.assertEqual(solution("z-y-x-w-v"), "26-25-24-23-22")
        
    def test5(self):
        self.assertEqual(solution("a-26-b-25-c-24"), "1-z-2-y-3-x")
        
    def test6(self):
        self.assertEqual(solution("13-9-14-15"), "m-i-n-o")
    
    def test7(self):
        self.assertEqual(solution("12-1-18-9-1"), "l-a-r-i-a")
        
    def test8(self):
        self.assertEqual(solution("19-15-12-21-20-9-15-14"), "s-o-l-u-t-i-o-n")
        
    def test9(self):
        self.assertEqual(solution("a-b-c-1-2-3-x-y-z-24-25-26"), "1-2-3-a-b-c-24-25-26-x-y-z")
        
    def test10(self):
        self.assertEqual(solution("16-9-20-8-15-14-3-8-1-18-13-1"), "p-i-t-h-o-n-c-h-a-r-m-a")

if __name__ == "__main__":
    unittest.main()