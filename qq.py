# create a function that takes two arguments, a certain figure and the second to be a percentage to be deducted from the first figure and return the subtracted result
def getSalary(money,taxP):
    tax = (taxP/100) * money
    return f"{money- tax} naira"
print(getSalary(23300,5))
# create a function that checks if a word is a palindrome
def isPalindrome(word):
    return word == word[::-1]

print(isPalindrome('dudu'))
print(isPalindrome('boob'))