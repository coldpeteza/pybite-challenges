import re
def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    line_count = 0
    char_count = 0
    word_count = 0
    with open(file_) as f:
        content = f.read()
        for line in content.splitlines(keepends=True):
            words = line.split()
            line_count += 1
            word_count += len(words)
            char_count += len(line)

    return f"{line_count} {word_count} {char_count} {f.name}\n"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))