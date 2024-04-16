INDENTS = 4
# part of Remember, by Christina Rosetti
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    indent_flag = True
    for line in poem.split('\n'):
        trimmed = line.strip()
        # print(f"{len(trimmed)}", end=' - ')
        if indent_flag:
            skip_blank_lines(trimmed)
            if len(trimmed) != 0:
                indent_flag = False
        else:
            if len(trimmed) == 0:
                indent_flag = True
                continue
            skip_blank_lines(" " * INDENTS + f"{trimmed}")


def skip_blank_lines(line):
    if line:
        print(f"{line}")


print_hanging_indents(rosetti_unformatted)
