"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import re

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word: str) -> bool:
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    result = re.sub(r'[\W\s]', '', word)
    return result.lower() == result[::-1].lower()


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = load_dictionary()

    max_palindrome = 0
    longest_palindrome = ''
    for word in words:
        if is_palindrome(word):
            if max_palindrome < len(word):
                max_palindrome = len(word)
                longest_palindrome = word

    return longest_palindrome
