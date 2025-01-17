# https://learn.codesignal.com/course/93/unit/2/practice/2

# You are given a string of n words, with n ranging from 1 to 100, inclusive. The words are separated by a single space in the string. Your task is to return the most frequently occurring character in each word that has an odd number of characters. The resulting characters should be concatenated into a string with their occurrences in the sentence.

# Please note:

# Each word's character count ranges from 1 to 500, inclusive. The string contains lowercase and uppercase alphanumeric characters, spaces, and punctuation.
# For instance, if the input string is "Hello world this is a demo string", your function should return "lwa". In this string, 'Hello', 'world', and 'a' have an odd number of characters. The most frequently occurring character in these words are 'l', 'w', and 'a' respectively. When concatenated, they form "lwa".
# In case of a tie in character frequency, return the character that appears first in the word. In the example above, we took 'w' from the word 'world'.
# The function should be case insensitive. The lowercase and uppercase characters should be counted as the same character. The output should only contain lowercase characters. For example: "Hhi" should return "h" because "h" appears twice in the string even though one is uppercase and one is lowercase.
# If there are no words with an odd number of characters in the input string, your function should return an empty string.
# The input string will always be at least one character long, and it cannot be just a single whitespace.
# Having a good understanding of string operations and the use of nested loops is very useful in solving this task.

def solution(sentence):
    result = []
    for word in sentence.split():
        if len(word) % 2 == 1:  # only process odd-length words
            # Create frequency map (case insensitive)
            char_freq = {}
            word_lower = word.lower()
            for char in word_lower:
                char_freq[char] = char_freq.get(char, 0) + 1
            
            # Find the most frequent character
            max_freq = 0
            first_max_char = None
            for char in word_lower:  # iterate in order to handle ties
                if char_freq[char] > max_freq:
                    max_freq = char_freq[char]
                    first_max_char = char
            
            result.append(first_max_char)
    
    return ''.join(result)

print(solution("Hello world this is a demo string")) # "lwa"

import unittest

class TestSolution(unittest.TestCase):

    def test1(self):
        # In the given sentence, the words "a", "programming" have an odd number of characters. 
        # The most frequently occurring character in "a", "programming" are "a" and "r" respectively.
        self.assertEqual(solution("Python is a high-level programming language"), "ar")

    def test2(self):
        # In the given sentence, the words "Mastering", "Looping", and "and" have an odd number of characters. 
        # The most frequently occurring character in "Mastering", "Looping", and "and" are "m", "o", and "a" respectively.
        self.assertEqual(solution("Mastering Advanced Looping and Implementation"), "moa")

    def test3(self):
        # In the given sentence, the word "loops" has an odd number of characters. 
        # The most frequently occurring character in "loops" is "o".
        self.assertEqual(solution("nested loops"), "o")

    def test4(self):
        # In the given sentence, the word "a" has an odd number of characters. 
        # The most frequently occurring character is "a" in "a".
        self.assertEqual(solution("Python provides us with a built-in"), "a")

    def test5(self):
        # In the given sentence, the words "navigated", "through" have odd number of characters.
        # The most frequently occurring character in "navigated" is "a" and in "through" is "h".
        self.assertEqual(solution("Bravo! You've just successfully navigated through"), "ah")

    def test6(self):
        # In the given sentence, the words "use", "knowledge", "a", "exploration", "loops" have odd number of characters. 
        # The most frequently occurring character in these words are "u", "e", "a", "o", "o" respectively.
        self.assertEqual(solution("Now, use this knowledge as a foundation in your exploration of nested loops"), "ueaoo")

    def test7(self):
        # In the given sentence, the words "Isn't", "fascinating" have odd number of characters. 
        # The most frequently occurring character in these words are "i" and "a" respectively.
        self.assertEqual(solution("Isn't it fascinating"), "ia")

    def test8(self):
        # The input string is a single word with an even number of characters, so the result is "".
        self.assertEqual(solution("Python"), "")

    def test9(self):
        # The input string is a single character string, so the result "a".
        self.assertEqual(solution("a"), "a")

    def test10(self):
        # The input string is a single word with an even number of characters, so the result is "".
        self.assertEqual(solution("high-level"), "") 

if __name__ == "__main__":
    unittest.main()