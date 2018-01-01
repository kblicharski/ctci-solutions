"""
Problem:
    There are three types of edits that can be performed on strings: insert
    a character, remove a character, or replace a character. Given two
    strings, write a function to check if they are one edit (or zero edits)
    away.

Implementation:

Efficiency:
    Time:
    Space:

"""


def ord_sum(string: str) -> int:
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
    str1 = str1.lower()
    str2 = str2.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str1_value = ord_sum(str1)
    str2_value = ord_sum(str2)
    ascii_values = {ord(c) for c in alphabet}
    difference = abs(str1_value - str2_value) 

    # This handles insertion and deletion
    # We just need a third check for replacement
    if difference in ascii_values or difference == 0:
        return True

    s1_chars = {c for c in str1}
    s2_chars = {c for c in str2}

    count = 0
    for c in s1_chars:
        if c in s2_chars:
            count += 1

    return len(str1) - count <= 1

# Zero edits
assert one_away('pale', 'pale') == True

# Removal
assert one_away('pale', 'ple') == True

# Insertion
assert one_away('pales', 'pale') == True

# Replacement
assert one_away('pale', 'bale') == True

assert one_away('pale', 'bake') == False 
