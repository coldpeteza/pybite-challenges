def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    bad_characters = [bad_char for bad_char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
    new_string = ""
    for char in input_string:
        if char in bad_characters:
            continue
        else:
            new_string += char
    return new_string
