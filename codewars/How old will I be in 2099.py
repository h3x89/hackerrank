# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python

# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.

# Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.

# Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"

# "..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

# Good Luck!

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
        return "You were born this very year!"
    elif age > 0:
        return f"You are {age} year{'s' if age > 1 else ''} old."
    else:
        return f"You will be born in {abs(age)} year{'s' if abs(age) > 1 else ''}."
    
import unittest

class TestCalculateAge(unittest.TestCase):
    def test_future_age(self):
      self.assertEqual(calculate_age(2012, 2016), "You are 4 years old.")
    
    def test_past_age(self):
      self.assertEqual(calculate_age(2000, 1990), "You will be born in 10 years.")
    
    def test_same_year(self):
      self.assertEqual(calculate_age(2000, 2000), "You were born this very year!")
    
    def test_one_year_old(self):
      self.assertEqual(calculate_age(2000, 2001), "You are 1 year old.")
    
    def test_one_year_until_birth(self):
      self.assertEqual(calculate_age(2001, 2000), "You will be born in 1 year.")

if __name__ == "__main__":
  unittest.main()