"""Given two strings, write a function to return True if the strings are anagrams of each other and False if they are not.
A word is not an anagram of itself.
"""

def is_anagram(string1, string2):
    if string1 == string2 or len(string1) != len(string2):
        return False
    string1_list = sorted(string1)
    string2_list = sorted(string2)
    return string1_list == string2_list

string_1 = "listen"
string_2 = "silent"
print(is_anagram(string_1, string_2))

string_1 = "banana"
string_2 = "bandana"
print(is_anagram(string_1, string_2))

string_1 = "banana"
string_2 = "banana"
print(is_anagram(string_1, string_2))
