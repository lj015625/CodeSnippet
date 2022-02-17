#O(n) time O(1) space
def isPalindrome(string):
    if len(string) == 1:
        return True
    leftIndex = 0
    rightIndex = len(string) - 1
    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightIndex]:
            return False
        else:
            leftIndex += 1
            rightIndex -= 1
    return True

print(isPalindrome("abcdcba"))

#O(n) time O(n) space
def isPalindrome2(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome2(string, i + 1)
print(isPalindrome2("abcdcba"))


#O(n) time O(n) space
def isPalindrome3(string):
    reversedChars = []
    for i in range(len(string)-1, -1, -1):
        reversedChars.append(string[i])
    return string == ''.join(reversedChars)
print(isPalindrome3("abcdcba"))
