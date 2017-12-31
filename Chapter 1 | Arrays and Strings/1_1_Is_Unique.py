"""
An algorithm to determine if a string of size N has all unique characters.

Characters are added iteratively to a set. If I were unable to use a set,
I would probably implement my own hash table and use that instead.

Time: O(N)
Space: O(N) 
"""


def is_unique(string: str) -> bool:
    char_set = set()
    for char in string:
        char_set.add(char)
    return len(char_set) == len(string)


assert is_unique('abc') == True
assert is_unique('a') == True
assert is_unique('') == True
assert is_unique('aac') == False
assert is_unique('aacc') == False
