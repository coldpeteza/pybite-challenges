from itertools import combinations


def find_number_pairs(numbers, N=10):
    results = []

    combos = combinations(numbers, 2)

    for combo in combos:
        if sum(combo) == N:
            results.append(combo)

    return results
