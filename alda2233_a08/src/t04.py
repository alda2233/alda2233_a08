"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-11"
-------------------------------------------------------
"""
# Imports
from asa import valid_isbn
# Constants
user_input = input("Enter an ISBN: ")
result = valid_isbn(user_input)
print(result)
