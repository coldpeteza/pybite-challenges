from typing import List
import re


def get_index_different_char(chars: List[str]) -> int:
    alpha_count = 0
    non_alpha_count = 0
    alpha_position_list = []
    non_alpha_position_list = []

    alpha_regex = re.compile(r'\w')
    for position, char in enumerate(chars):
        match_found = re.match(alpha_regex, str(char))
        if match_found is None:
            non_alpha_count += 1
            alpha_position_list.append((position, char))
        else:
            alpha_count += 1
            non_alpha_position_list.append((position, char))

    if alpha_count < non_alpha_count:
        return non_alpha_position_list.pop()[0]
    else:
        return alpha_position_list.pop()[0]

# if __name__ == '__main__':
#     print(get_index_different_char(['A', 'f', '.', 'Q', 2]))