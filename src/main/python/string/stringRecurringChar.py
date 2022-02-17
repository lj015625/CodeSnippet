"""Given a string, write a function recurring_char to find its first recurring character. Return None if there is no recurring character.
Treat upper and lower case letters as distinct characters.
You may assume the input string includes no spaces."""


def recurring_char(input):
    seen = set()
    for char in input:
        if char in seen:
            return char
        seen.add(char)

    return None


input = "interviewquery"
print(recurring_char(input))

input = "interv"
print(recurring_char(input))
