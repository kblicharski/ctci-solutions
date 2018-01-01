"""
Problem:

Implementation:

Efficiency:
    Time:
    Space:

"""

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
    pass



# Zero edits
assert one_away('pale', 'pale') == True

# Removal
assert one_away('pale', 'ple') == True

# Insertion
assert one_away('pales', 'pale') == True

# Replacement
assert one_away('pale', 'bale') == True

assert one_away('pale', 'bake') == False 
