"""
Python version 3.7.0
1.9 - String Rotation
Assume you have a method isSubstring which
checks if one word is a substring
of another.  Given two strings, s1 and s2,
write code to check if s2 is a
rotation of s1 using only one call to isSubstring
(e.g. 'waterbottle' is a rotation of 'erbottlewat')
"""
import unittest


def is_substring(sub: str, s: str) -> bool:
    """
    is_substring checks if 'sub' is a substring of 's'
    :param sub: the substring
    :param s: the alleged full string
    :return: true if sub is a substring of s, false otherwise
    """
    return sub in s


def string_rotation(s1: str, s2: str) -> bool:
    """
    Given two strings, string_rotation will check if s2 is a rotation of s1
    using only one call to isSubstring.
    If s2 is a rotation of s1, then when we add s1 to itself, s2
    must be a substring of s1 + s1
    Runtime: O(n)
    Space Complexity:  O(1)
    :param s1: the rotated string
    :param s2: the original string
    :return: true if s2 is a rotation of s1, false otherwise
    """
    # not rotation if lengths don't match
    if len(s1) != len(s2):
        return False
    return is_substring(s2, s1 + s1)


class TestStringRotation(unittest.TestCase):

    def setUp(self):
        self.str_rotation_cases = [
            ('erbottlewat', 'waterbottle', True),
            ('erbottlewet', 'weterbottle', True),
            ('same', 'same', True),
            ('oneoff', 'oneof', False),
            ('erbottleabc', 'waterbottle', False),
            ('ion?rotat', 'rotation?', True),
            ('', '', True),
            ('a', 'a', True),
            ('a', 'b', False),
            ('erbottlewat', 'eeeeeeeeee', False)
        ]

        self.is_substring_cases = [
            ('swag', 'swagger', True),
            ('swagger', 'swag', False),
            ('test', 'testing', True),
            ('', 'sdfkjslf', True),
            ('abcd', 'defg', False)
        ]

    def test_is_substring(self):
        for sub, s, expected in self.is_substring_cases:
            self.assertEqual(is_substring(sub, s), expected, msg=(sub, s, expected))

    def test_string_rotation(self):
        for s1, s2, expected in self.str_rotation_cases:
            self.assertEqual(string_rotation(s1, s2), expected, msg=(s1, s2, expected))


if __name__ == '__main__':
    unittest.main()
