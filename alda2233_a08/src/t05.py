"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain
# Constants


words_input = input("Enter a list of words separated by spaces: ")
words = words_input.split()

# Test the function
result = has_word_chain(words)
print(result)
