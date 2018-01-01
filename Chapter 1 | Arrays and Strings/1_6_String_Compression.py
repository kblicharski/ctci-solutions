"""
Problem:
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string 'aabcccccaaa' would
    become 'a2b1c5a3'. If the "compressed" string would not become smaller
    than the original string, your method should return the original
    string. You can assume the string has only uppercase and lowercase
    letters (a-z).

Implementation:
    TODO

Efficiency:
    Time:
    Space:

"""


def compressed_string(string: str) -> str:
    """
    Compress a string using the counts of its repeated characters, if possible.

    Args:
        string (str): The string to be compressed.

    Returns:
        str: The compressed string if its size is smaller than the original.

    Examples:
        >>> compressed_string('aabcccccaaa')
        'a2b1c5a3'
        >>> compressed_string('abcdd')
        'abcdd'

    """
    return string
