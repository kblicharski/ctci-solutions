"""
Problem:
    Implement an algorithm to determine if a string has all
    unique characters. What if you cannot use additional data structures?

Implementation:
    Characters are added iteratively to a set. If I could not use a set,
    I would probably implement my own hash table, using a list and
    "hashing" the ASCII value of the characters, and use that instead.

Efficiency:
    Time: O(N)
    Space: O(N)

"""


def is_unique(string: str) -> bool:
    """
    Determine if a string of size N has all unique characters.

    Args:
        string (str): The string we are checking.

    Returns:
        bool: True if the string has all unique characters.

    """
    char_set = set()
    for char in string:
        char_set.add(char)
    return len(char_set) == len(string)


assert is_unique('abc')
assert is_unique('a')
assert is_unique('')
assert not is_unique('aac')
assert not is_unique('aacc')
