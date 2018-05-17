# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

import re


def longestWord(text):
    return max(re.compile(r'\W').text.split(text), key=len)
