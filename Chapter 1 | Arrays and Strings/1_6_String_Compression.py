"""
Problem:
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string 'aabcccccaaa' would
    become 'a2b1c5a3'. If the "compressed" string would not become smaller
    than the original string, your method should return the original
    string. You can assume the string has only uppercase and lowercase
    letters (a-z).

Implementation:
    We can return early if our string is under 3 characters long, because
    there is no way that compression would benefit it. Otherwise, we need to
    traverse the string and count the number of consecutive characters,
    appending them to the list that stores the "tokens" of our compressed
    string. We then finally join the tokens back into a string and compare
    the lengths of our compressed string and our original string to determine
    which should be returned.

    Because we have to traverse the original string in O(N) time, and then
    join the compressed string in (worst case, when we have all unique
    characters) O(2N) time, the total runtime is linear.

Efficiency:
    Time: O(N)
    Space: O(N)

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
    if len(string) < 3:
        return string

    compressed_chars = []
    count = 1
    for i, c in enumerate(string):
        try:
            if c == string[i + 1]:
                count += 1
            else:
                compressed_chars.append(c)
                compressed_chars.append(str(count))
                count = 1
        except IndexError:
            compressed_chars.append(c)
            compressed_chars.append(str(count))

    compressed_str = ''.join(compressed_chars)
    if len(compressed_str) < len(string):
        return compressed_str
    return string


assert compressed_string('') == ''
assert compressed_string('a') == 'a'
assert compressed_string('aa') == 'aa'
assert compressed_string('aaa') == 'a3'
assert compressed_string('abc') == 'abc'
assert compressed_string('abcdefgh') == 'abcdefgh'
assert compressed_string('aabcccccaaa') == 'a2b1c5a3'
assert compressed_string('abcdd') == 'abcdd'
