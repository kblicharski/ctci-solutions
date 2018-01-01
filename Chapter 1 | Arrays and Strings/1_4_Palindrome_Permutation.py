"""
Problem:
    Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word or phrase that is the same forwards
    and backwards. A permutation is a rearrangement of letters. The
    palindrome does not need to be limited to just dictionary words.

    Example:
        Input: Tact Coa
        Output: True (permutations: 'taco cat', 'atco cta', etc.)

Implementation:
    The problem statement only says we have to check that it IS a
    permutation of a palindrome, not that we need to find all of these
    viable permutations. We could check every possible combination of
    letters and see if each one of these is a palindrome, but that would
    be O(N!). Instead, we should rely on the definition of a palindrome.

    A palindrome is the same forwards and backwards. This means that, among
    our unique characters, we need to have them paired, with the exception
    of maybe one character that is sandwiched in the middle. This will
    be the intuition we need.

    We can add characters onto a set the first time we see them, and
    remove them when we see them again. Once we've looked at all of our
    characters, we just need to verify that our set has at most one
    character in it.

Efficiency:
    Time: O(N)
    Space: O(N)

"""


def palindrome_permutation(string: str) -> bool:
    """
    Determine if a string has a permutation that makes it a palindrome.

    Args:
        string (str): The string we are checking.

    Returns:
        bool: True if the string has a viable permutation.

    """
    characters = set()
    for c in string:
        if c in characters:
            characters.remove(c)
        else:
            characters.add(c)
    return len(characters) <= 1


# 'a'
assert palindrome_permutation('a') == True
assert palindrome_permutation('ab') == False

# 'aba'
assert palindrome_permutation('baa') == True
assert palindrome_permutation('baac') == False 

# 'abba', 'baab'
assert palindrome_permutation('abba') == True
assert palindrome_permutation('abaa') == False

# 'abcba', 'bacab'
assert palindrome_permutation('abcba') == True
assert palindrome_permutation('abccca') == False
