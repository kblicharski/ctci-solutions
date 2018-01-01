"""
Problem:
    There are three types of edits that can be performed on strings: insert
    a character, remove a character, or replace a character. Given two
    strings, write a function to check if they are one edit (or zero edits)
    away.

Implementation:
    An initial solution might check for all three cases separately. In my
    solution, I decided to go with using the ASCII values of the letters
    to determine whether they were within the edit distance. This worked
    very well for the insertion and deletion cases, but failed for
    replacement.

    For replacement, we have to add the letters of each string into sets.
    We then take the set difference. If the set difference has one or no
    characters remaining, then we know we're within one replacement.
    Otherwise, we would have to replace more than one character, and we
    can return false.

Efficiency:
    Time: O(A + B)
    Space: O(A + B)

"""


def ord_sum(string: str) -> int:
    """
    Sum the ASCII values of the characters of a passed string.

    Args:
        string (str): The string whose ASCII values we are summing.

    Returns:
        int: The sum of each letter's ASCII value.

    """
    return sum([ord(c) for c in string])


def one_away(str1: str, str2: str) -> bool:
    """
    Check if the first string is at most one 'edit' away from the second.

    An 'edit' is defined as a character insertion, deletion,
    or replacement.

    Args:
        str1 (str): The first string we are checking.
        str2 (str): The second string we are checking.

    Returns:
        bool: True if string one is at most one 'edit' away from the other.

    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_values = {ord(c) for c in alphabet}

    str1_value = ord_sum(str1)
    str2_value = ord_sum(str2)
    difference = abs(str1_value - str2_value)

    # The strings are the same.
    if difference == 0:
        return True
    # The strings are one insertion or deletion apart.
    if difference in ascii_values:
        return True
    # The strings are one replacement apart.
    s1_chars = {c for c in str1}
    s2_chars = {c for c in str2}
    return len(s1_chars - s2_chars) <= 1


# Zero edits
assert one_away('pale', 'pale')

# Removal
assert one_away('pale', 'ple')

# Insertion
assert one_away('pales', 'pale')

# Replacement
assert one_away('pale', 'bale')

# Two replacements apart
assert not one_away('pale', 'bake')

# One string is two characters longer
assert not one_away('palest', 'bake')
