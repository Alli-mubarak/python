def sumUp(a, b):
    return a + b
def subtract(a, b):
    if a > b:
        return a - b
    return 'error'
# print(sumUp(3,6))
# print(subtract(4, 9))
# print(subtract(10, 2))
def multiply(a, b):
    return a * b
def divide(a, b):
    if b > a :
        return 'error'
    return a / b
# print(multiply(9,4))
# print(divide(9, 2))
# print(divide(5, 22))
def unveil(list):
    for item in list:
        print(item)
a_list = ['loop', 'joule', 'johnie']
unveil(a_list)
text = 'i will love you very well'
def detail(str):
   br_text =  str.split()
   print(br_text)
detail(text)
def is_palindrome(text):
    rev = text[::-1]
    if rev == text:
        return f'i am a palindrome because {text} is the same as {rev}'
    else:
        return f'i am not a palindrome because {text} is not the same as {rev}'
print(is_palindrome("goon"))
print(is_palindrome('noon'))
print(is_palindrome('alias'))