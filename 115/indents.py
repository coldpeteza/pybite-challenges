def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    whitespace_removed = text.strip(' ')
    first_char = whitespace_removed[0]
    first_character_index = text.index(first_char)

    return first_character_index
