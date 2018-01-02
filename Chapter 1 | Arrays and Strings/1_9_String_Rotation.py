"""
Problem:
    Assume you have a method is_substring which checks if one word is a
    substring of another. Given two strings, s1 and s2, write code to check
    if s2 is a rotation of s1 using only one call to is_substring (e.g.,
    'waterbottle' is a rotation of 'erbottlewat'.

Implementation:
    This problem is basically a brain-teaser and relies on one key piece of
    insight that might be difficult to catch immediately.
    s1 is a rotation of s2 only if s1 is contained in s2 appended to itself. In
    the above example, this becomes clear after looking at the string
    'erbottlewaterbottlewat'. 'waterbottle' is contained inside.

    We need to avoid the O(N^2) time of string concatenation, so in Python this
    would mean using the str.join method, or for shorthand, just multiplying
    s1 by two.

Efficiency:
    Time: O(A+B)
    Space: O(B)

"""


def string_rotation(s1: str, s2: str) -> bool:
    """
    Check if the second string is a rotation of the first string.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the second string is a rotation of the first.

    """
    return len(s1) == len(s2) and s1 in s2*2


assert string_rotation('', '')
assert string_rotation('a', 'a')

assert string_rotation('ab', 'ba')

assert string_rotation('aba', 'aab')
assert string_rotation('aba', 'baa')
assert string_rotation('aba', 'aba')

assert string_rotation('abc', 'cab')
assert string_rotation('abc', 'bca')
assert string_rotation('abc', 'abc')

assert not string_rotation('abc', 'cba')
assert not string_rotation('abc', 'acb')
assert not string_rotation('abc', 'bac')

assert string_rotation('abaa', 'aaba')
assert string_rotation('abaa', 'aaab')
assert string_rotation('abaa', 'baaa')

assert string_rotation('waterbottle', 'erbottlewat')
assert not string_rotation('waterbottle', 'werbottleat')
assert not string_rotation('waterbottle', 'erwbottleat')
