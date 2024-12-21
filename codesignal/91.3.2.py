# https://learn.codesignal.com/course/91/unit/3/practice/2

# You are provided with a string of n lowercase English alphabet letters (from 'a' to 'z'), where n ranges from 1 to 100, inclusive. You must create a new string by selecting characters from the given string in a specific order: select each character that comes k characters after the previous selection in the string. If you reach the end of the string, you should continue from the beginning.

# Write a Python function, repeat_char_jump(inputString, step). The function takes two parameters: inputString and step, where inputString is the string you are working with, and step is an integer that denotes the number of characters to skip with each jump. The value of step ranges from 1 to the length of the input string. The function should return a newly formed string consisting of characters selected in the order dictated by the jump length step.

# For example, if inputString is "abcdefg" and step is 3, the function should return "adgcfbe". This is because after 'a', comes 'd' (3 characters after 'a'), followed by 'g' (3 characters after 'd', circling back to the start of the string after 'g'), and so on.

# Note: You should continue jumping from the start of the string when you reach the end.

# For this task, assume that you need not use a character more than once. When you have traversed all the characters at least once, you can stop and return the output string as it is. It is guaranteed, that the inputs will be given in a way, that following the traversal pattern, you'll traverse all the characters.

def repeat_char_jump(inputString, step):
    n = len(inputString)
    visited = [False] * n
    output = ""
    current_pos = 0
    
    # Continue until all characters are visited
    while len(output) < n:
        if not visited[current_pos]:
            output += inputString[current_pos]
            visited[current_pos] = True
        current_pos = (current_pos + step) % n
        
    return output

print(repeat_char_jump("abcdefg", 3))

import unittest

class TestRepeatCharJump(unittest.TestCase):
    def test1(self):
        self.assertEqual(repeat_char_jump("abcdefg", 3), "adgcfbe")

    def test2(self):
        self.assertEqual(repeat_char_jump("a", 1), "a")

    def test3(self):
        self.assertEqual(repeat_char_jump("av", 1), "av")
        
    def test4(self):
        self.assertEqual(repeat_char_jump("cgldxdv", 4), "cxgdlvd")
        
    def test5(self):
        self.assertEqual(repeat_char_jump("z", 1), "z")
        
    def test6(self):
        self.assertEqual(repeat_char_jump("aaa", 2), "aaa")
        
    def test7(self):
        self.assertEqual(repeat_char_jump("zyxwvutsrqponmlkjihgfedcba", 5), "zupkfavqlgbwrmhcxsnidytoje")
        
    def test8(self):
        self.assertEqual(repeat_char_jump("zyxwvutsrqponmlkjihgfedcba", 15), "zkvgrcnyjufqbmxitepalwhsdo")
        
    def test9(self):
        self.assertEqual(repeat_char_jump("abcdefghij", 1), "abcdefghij")
        
    def test10(self):
        self.assertEqual(repeat_char_jump("abcdefghij", 9), "ajihgfedcb")

if __name__ == "__main__":
    unittest.main()