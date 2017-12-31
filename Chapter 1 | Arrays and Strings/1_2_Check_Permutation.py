"""
An algorithm to determine if one string of size A is a permutation of
another string of size B.

If the strings are not the same size, we can return early.
Otherwise, we just need to check that they share the same unique characters.

Time: O(A + B)
Space: O(A + B)
"""


def check_permutation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    char_set1 = set()
    char_set2 = set()
    for c in str1:
        char_set1.add(c)
    for c in str2:
        char_set2.add(c)
    return len(char_set1) == len(char_set2)


assert check_permutation('a', 'a') == True
assert check_permutation('ab', 'ba') == True
assert check_permutation('aba', 'baa') == True
assert check_permutation('abba', 'baab') == True
assert check_permutation('aa', 'ba') == False
assert check_permutation('a', 'b') == False
