"""
Problem:
    Given two strings, write a method to decide if one is
    a permutation of the other.

Implementation:
    A string of size A is a permutation of another string of size B if:
        1. They have the same length.
        2. They have the same unique characters.
        3. They have the same number of unique characters.

    All we have to do is encode those constraints into an algorithm.

Efficiency:
    Time: O(A + B)
    Space: O(A + B)

"""


def check_permutation(str1: str, str2: str) -> bool:
    """
    Determine if one string is a permutation of the other.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if string one is a permutation of string two.

    """
    # Check the lengths.
    if len(str1) != len(str2):
        return False

    # Check the unique characters.
    chars1 = {c: 0 for c in str1}
    chars2 = {c: 0 for c in str2}

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


assert check_permutation('a', 'a')
assert check_permutation('ab', 'ba')
assert check_permutation('aba', 'baa')
assert check_permutation('abba', 'baab')
assert not check_permutation('aa', 'a')
assert not check_permutation('aab', 'bba')
assert not check_permutation('aa', 'ba')
assert not check_permutation('a', 'b')
