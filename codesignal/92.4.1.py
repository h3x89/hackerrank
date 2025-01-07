# https://learn.codesignal.com/course/92/unit/4/practice/1

# Imagine you are working on a new feature for a text processing application. The feature requires you to provide users with the option to replace all occurrences of a certain substring in the entered text with a new substring.

# You are tasked with writing a function, replace_substring(text: str, old: str, new: str) -> str, that does the following:

# Accepts as input text (a string of length n, where 1 ≤ n ≤ 500, which includes only lowercase alphabets and spaces), old (a string of length k, where 1 ≤ k ≤ n, which includes only lowercase alphabets), and new (a string of length m, where 1 ≤ m ≤ 500, which includes only lowercase alphabets).

# Replaces every occurrence of the string old in text with the string new.

# Returns the updated text string with all replaced substrings.

# Please ensure that the case of the letters remains consistent during the process, meaning an uppercase letter should be replaced with an uppercase letter, and a lowercase letter should be replaced with a lowercase one.

# For instance, your function might be called as follows:

# Python
# Copy to clipboard
# replace_substring("hello world", "world", "friend")
# In this case, the output would be:

# Copy to clipboard
# "hello friend"
# This is because there is one occurrence of the substring 'world' in the string. This occurrence is replaced by 'friend', resulting in the return value "hello friend".

def replace_substring(text, old, new):
    return new.join(text.split(old))

print(replace_substring("hello world", "world", "friend")) # "hello friend"

import unittest

class ReplaceSubstringTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(replace_substring("hello world", "world", "friend"), "hello friend")

    def test_2(self):
        self.assertEqual(replace_substring("i love coding", "code", "craft"), "i love coding")

    def test_3(self):
        self.assertEqual(replace_substring("it is a beautiful day", "beautiful", "gloomy"), "it is a gloomy day")

    def test_4(self):
        self.assertEqual(replace_substring("practice makes perfect", "perfect", "better"), "practice makes better")

    def test_5(self):
        self.assertEqual(replace_substring("keep calm and carry on", "carry on", "code on"), "keep calm and code on")

    def test_6(self):
        self.assertEqual(replace_substring("long text long text", "long", "short"), "short text short text")

    def test_7(self):
        self.assertEqual(replace_substring("lower case", "lower", ""), " case")

    def test_8(self):
        self.assertEqual(replace_substring("a quick brown fox jumps over a lazy dog", "jumps", "skips"), "a quick brown fox skips over a lazy dog")

    def test_9(self):
        self.assertEqual(replace_substring("this is a test", "this", "that"), "that is a test")

    def test_10(self):
        self.assertEqual(replace_substring("final test case", "case", "example"), "final test example")

if __name__ == "__main__":
    unittest.main()