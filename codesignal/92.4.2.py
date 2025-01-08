# https://learn.codesignal.com/course/92/unit/4/practice/2

# You are given two lists, sentences and words, each comprising n strings, where n ranges from 
# 1 to 100 inclusive. Each string in the sentences list has a length ranging from 
# 1 to 500 inclusive. Each word in the words list is a single lowercase English alphabet word of length 
# 1 to 10 inclusive.

# Your task is to find all instances of each word in the corresponding sentence from the sentences list and replace them with the reverse of the word. The words and sentences at the same index in their respective lists are deemed to correspond to each other.

# Return a new list comprising n strings, where each string is the sentence from the sentences list at the corresponding index, with all instances of the word from the words list at the same index replaced with its reverse.

# If the word is not found in the respective sentence, keep the sentence as it is.

# Remember, while replacing the instances of word in the sentence, you should preserve the case of the initial letter of the word. If a word starts with a capital letter in the sentence, its reversed form should also start with a capital letter.

# Example

# For sentences = ['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'] and words = ['simple', 'bond', 'e'], the output should be ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'].

def solution(sentences, words):
    res = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        word = words[i]
        
        # Find all occurrences of the word (case-insensitive)
        import re
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        
        def replace_func(match):
            matched_word = match.group(0)
            reversed_word = word[::-1]
            # Preserve case of first letter
            if matched_word[0].isupper():
                reversed_word = reversed_word.capitalize()
            else:
                reversed_word = reversed_word.lower()
            return reversed_word
            
        new_sentence = pattern.sub(replace_func, sentence)
        res.append(new_sentence)
    
    return res

print(solution(['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'], ['simple', 'bond', 'e'])) # ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e']

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(['this is a simple example.', 'the name is bond. james bond.', 'remove every single e'], ['simple', 'bond', 'e']), ['this is a elpmis example.', 'the name is dnob. james dnob.', 'remove every single e'])
        
    def test2(self):
        self.assertEqual(solution(['hello world!', 'i am here', 'python is love'], ['world', 'here', 'love']), ['hello dlrow!', 'i am ereh', 'python is evol'])
        
    def test3(self):
        self.assertEqual(solution(['i am not a robot', 'you are not alone', 'we are all together'], ['am', 'are', 'are']), ['i ma not a robot', 'you era not alone', 'we era all together'])
        
    def test4(self):
        self.assertEqual(solution(['apple', 'ball', 'cat'], ['a', 'b', 'c']), ['apple', 'ball', 'cat'])
        
    def test5(self):
        self.assertEqual(solution(['this is a test', '', '', 'one more'], ['test', 'a', 'b', 'one']), ['this is a tset', '', '', 'eno more'])
        
    def test6(self):
        self.assertEqual(solution(['lower case sentence', 'upper case Sentence', 'another Sentence here', 'final Sentence yay'], ['sentence', 'sentence', 'sentence', 'sentence']), ['lower case ecnetnes', 'upper case Ecnetnes', 'another Ecnetnes here', 'final Ecnetnes yay'])
        
    def test7(self):
        self.assertEqual(solution(['this is a very very long sentence just to check the maximum limit of the sentence. see if it can handle the maximum characters or not.', 'can it handle', 'it or not', "let's see."], ['very', 'handle', 'it', 'see']), ['this is a yrev yrev long sentence just to check the maximum limit of the sentence. see if it can handle the maximum characters or not.', 'can it eldnah', 'ti or not', "let's ees."])
        
    def test8(self):
        self.assertEqual(solution(['just a string', 'with some words', 'and nothing else'], ['just', 'some', 'nothing']), ['tsuj a string', 'with emos words', 'and gnihton else'])

if __name__ == '__main__':
    unittest.main()