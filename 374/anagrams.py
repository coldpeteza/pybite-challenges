from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""

    d = defaultdict(list)
    for word in strings:
        d["".join(sorted(word))].append(word)

    return [item for item in d.values()]


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))