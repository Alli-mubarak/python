def getSquareRoot(n):
    return n ** 0.5
# print(getSquareRoot(144))
# print(getSquareRoot(49))
# print(getSquareRoot(11))
# print(getSquareRoot(1))
# print(getSquareRoot(2))

def isPalindrome(word):
    return word == word[::-1]
# print(isPalindrome("madam"))
# print(isPalindrome("kayak"))
# print(isPalindrome("madame"))
# print(isPalindrome("barley"))

def countLetters(word):
    return len(word)

print(countLetters("shopping"))