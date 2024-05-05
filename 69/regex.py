import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')
    results = pattern.search(text)
    return bool(results)


def is_integer(number):
    """Return True if number is an integer"""
    pattern = re.compile(r'[\-]?\d+$')
    result = re.match(pattern, str(number))
    return False if result is None else True


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = re.compile(r'(\-)+\w')
    result = re.search(pattern, text)
    return False if result is None else True


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = re.compile(r'\s\([a-z,0-9\.]+\)',re.IGNORECASE)
    result = re.sub(pattern, '', text)
    return result


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    pattern = re.compile(r'[\?\!\.\,\;\-]')
    items = re.split(pattern, text)
    results = []
    for item in items:
        if item:
            results.append(item.strip())
    return results


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pattern = re.compile(r'(?<=\s)\s+')
    result = re.sub(pattern, '', text)
    return result


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = re.compile('[aeiouAEIOU]{3}')
    result = re.search(pattern, word)
    return False if result is None else True


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    parts = re.search(pattern, date)
    result = 'none'
    if parts:
        day, month, year = parts.groups()
        result = f'{month}/{day}/{year}'
    return result
