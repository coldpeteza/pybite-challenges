def validate_pangram(sentence: str) -> bool:
    """Check if a sentence is a pangram
    A pangram is a sentence containing every letter in the English alphabet.
    The input `sentence` should be a string containing only English letters.
    The function returns True if the sentence is a pangram, and False otherwise.
    """
    pangram_sentence = set([letter.lower() for letter in sentence if letter.strip()])
    every_leter = set([chr(ord('a') + i) for i in range(26)])
    return every_leter.issubset(pangram_sentence)


if __name__ == "__main__":
    print(validate_pangram('The quick brown fox jumps over the lazy dog'))