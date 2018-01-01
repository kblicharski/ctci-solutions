"""
Problem:
    Write a method to replace all spaces in a string with '%20'. You may
    assume that the string has sufficient space at the end to hold the
    additional characters, and that you are given the "true" length of the
    string.

    Example:
        Input: "Mr John Smith     ", 13
        Output: "Mr%20John%20Smith"

Implementation:
    When using Python, this is very easy. We can rely on two built-in
    string methods to do this. If we were to do this in-place, it would be
    more complicated, but still not that difficult. The problem statement
    was unclear in whether we should strip leading and trailing spaces, but
    the given example was stripped, so I applied that as well.

Efficiency:
    Time: O(N)
    Space: O(1)

"""


def urlify(raw_string: str) -> str:
    """
    'URLifies' a string by replacing all spaces with '%20'.

    Args:
        raw_string (str): The string to URLify.

    Returns:
        str: The string with all spaces replaced with '%20'.

    """
    return raw_string.strip().replace(' ', '%20')


assert urlify('Mr John Smith     ') == 'Mr%20John%20Smith'
assert urlify('      Mr John Smith     ') == 'Mr%20John%20Smith'
assert urlify('Mr   John Smith     ') == 'Mr%20%20%20John%20Smith'
