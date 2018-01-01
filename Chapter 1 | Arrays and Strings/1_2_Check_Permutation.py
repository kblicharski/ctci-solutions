"""
An algorithm to determine if one string of size A is a permutation of
another string of size B.

A string is a permutation of another string if:
    1. They have the same length.
    2. They have the same unique characters.
    3. They have the same number of unique characters.

All we have to do is encode those constraints into an algorithm.

Time: O(A + B)
Space: O(A + B)
"""


def check_permutation(str1: str, str2: str) -> bool:
    # Check the lengths.
    if len(str1) != len(str2): return False

    # Check the unique characters.
    chars1 = {c:0 for c in str1}
    chars2 = {c:0 for c in str2}

    for c in chars1:
        if c not in chars2:
            return False

    # Sum the occurrences.
    for c in str1:
        chars1[c] += 1
    for c in str2:
        chars2[c] += 1

    # Check the occurrences.
    for c in chars1:
        if chars1[c] != chars2[c]:
            return False

    return True


assert check_permutation('a', 'a') == True
assert check_permutation('ab', 'ba') == True
assert check_permutation('aba', 'baa') == True
assert check_permutation('abba', 'baab') == True
assert check_permutation('aa', 'a') == False
assert check_permutation('aab', 'bba') == False
assert check_permutation('aa', 'ba') == False
assert check_permutation('a', 'b') == False
