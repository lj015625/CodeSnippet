"""Shift string characters by k position. letter should wrap around, z shifts one return a. """


def caesarCipherEncryptor(string, key):
    shiftedString = ""
    for char in string:
        unicode = (ord(char) - ord('a') + key) % 26 + ord('a')
        shiftedString = shiftedString + chr(unicode)
    return shiftedString


def caesarCipherEncryptor2(string, key):
    shifted = []
    newKey = key
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for char in string:
        newLetterCode = (alphabet.index(char) + newKey) % 26
        shifted.append(alphabet[newLetterCode])
    return ''.join(shifted)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("zab", caesarCipherEncryptor("xyz", 2))
        self.assertEqual("zab", caesarCipherEncryptor2("xyz", 2))
