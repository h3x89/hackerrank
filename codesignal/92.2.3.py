# https://learn.codesignal.com/course/92/unit/2/practice/3

# You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

# Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. All spaces and punctuation marks between the number and the letter are removed.

# The length of the string s ranges from 3 to 
# 1
# 0
# 6
# 10 
# 6
#   (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.

# Here is an example for better understanding:

# Given the string:

# "I have 2 apples and 5! oranges and 3 grapefruits."

# The function should return:

# "I have a2pples and o5ranges and g3rapefruits."

# In this instance, the character 'a' following the number 2 is moved to come before the 2, the 'o' succeeding the 5 is placed before the 5, and the 'g' subsequent to the 3 is repositioned to precede the 3. Punctuation marks and spaces in between are removed.

# Please note that the operation should maintain the sequential order of the numbers and the rest of the text. Considering this, the task is not solely about dividing a string into substrings but also about modifying them. This will test your expertise in Python string operations and type conversions.

def solution(input_string):
    result = []
    i = 0
    while i < len(input_string):
        # If we find a digit
        if input_string[i].isdigit():
            num = ''
            # Get the complete number
            while i < len(input_string) and input_string[i].isdigit():
                num += input_string[i]
                i += 1
            
            # Skip any non-letter characters
            while i < len(input_string) and not input_string[i].isalpha():
                i += 1
            
            # Get the first letter after the number
            if i < len(input_string):
                letter = input_string[i]
                result.append(letter + num)
                i += 1
        else:
            result.append(input_string[i])
            i += 1
    
    return ''.join(result)

print(solution("I have 2 apples and 5! oranges and 3 grapefruits."))

import unittest


class SolutionTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution("I have 2 apples and 5 oranges and 3 grapefruits."), "I have a2pples and o5ranges and g3rapefruits.")

    def test2(self):
        self.assertEqual(solution("4 foxes are chasing 1 rabbit."), "f4oxes are chasing r1abbit.")
 
    def test3(self):
        self.assertEqual(solution("Let's meet at 7 at the clock tower."), "Let's meet at a7t the clock tower.")

    def test4(self):
        self.assertEqual(solution("There are 8 wonders of the world."), "There are w8onders of the world.")

    def test5(self):
        self.assertEqual(solution("I will bring 6 bottles of water and 4 packets of chips."), "I will bring b6ottles of water and p4ackets of chips.")

    def test6(self):
        self.assertEqual(solution("It is a 9 day journey to the mountains."), "It is a d9ay journey to the mountains.")

    def test7(self):
        self.assertEqual(solution("She has lived in 4 cities and 2 countries."), "She has lived in c4ities and c2ountries.")

    def test8(self):
        self.assertEqual(solution("He walked 5 miles to school every day."), "He walked m5iles to school every day.")

    def test9(self):
        self.assertEqual(solution("The city has 6 gates."), "The city has g6ates.")

    def test10(self):
        self.assertEqual(solution("There are 3 books on the table."), "There are b3ooks on the table.")

if __name__ == '__main__':
    unittest.main()