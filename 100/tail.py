from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    result = []

    with filepath.open(encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    for i in range(n):
        try:
            result.append(lines.pop())
            result.reverse()
        except IndexError:
            result = filepath.read_text().splitlines()



    return result
