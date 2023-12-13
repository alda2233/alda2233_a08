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
from functions import add_spaces
# Constants

sentence = input(
    "Enter a sentence without spaces but with uppercase starting characters: ")
spaced_sentence = add_spaces(sentence)
print(spaced_sentence)
