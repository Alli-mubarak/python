# Q1
x = 5
y = "Hello"
z = True
print(type(x), type(y), type(z))
# Q2
def checkNum(num):
    if num % 2 == 1:
        return "Odd number"
    else:
        return "Even number"
    
print(checkNum(2))
print(checkNum(555))
# Q3
count = 1
while count < 11 :
    print(count)
    count += 1
# Q4
def getSum(list):
    return sum(list)

kk = [2, 4, 5, 22, 19]
print(getSum(kk))
# Q5
namesDictionary = {
    "person1":["John Kent", 23],
    "person2":["Sally Brown", 29],
    "person3":["Barry Kendrick", 43]
}
print(namesDictionary['person1'])
# Q6
def get_product(a, b):
    return a * b
print(get_product(2, 9))
# Q7 ----------Palindrome---
text = "a n drEw"
# print(text[::-1])

def check_palindrome(text):
    processed_text = text.lower().replace(" ", "")
    return processed_text == processed_text[::-1]
print(check_palindrome("madam"))
print(check_palindrome("madame"))

# Q8
def even_squared(list):
    new_num = [num * 2 for num in list if num % 2 == 0]
    return new_num

listOne = [2, 5, 4, 7, 9, 5, 10, 11, 12]
print(even_squared(listOne))

# Q9 ----Dictionary word counter--
worrd = "hello baby hello baby girl"
def dic_word_counter(sentence):
    word_list = sentence.split(" ")
    word_set = set(word_list)
    word_dic = {}
    for words in word_list:
        words.lower()
        if words in word_dic:
          word_dic[words] += 1
        else:
           word_dic[words] = 1
    return word_dic
# print(dic_word_counter(worrd))
new_sentence = "i am who i am and i love who i am because i will always be who i am"
print(dic_word_counter(new_sentence))
# Q10 _------factorial---
def factorial(n):
    # while n > 0:
    #  return n *(n - 1)
     if n == 0:
         return 1
     else:
         return n * factorial(n-1)
print(factorial(4))

# Q11  -- prime number checker -------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num1 = 7
num2 = 12
print(is_prime(num1))
print(is_prime(num2))

# print((7**0.5) + 1)

# Q12
def find_unique(numbers):
    # we can return uniq_list or unic
    num_set = set(numbers)
    uniq_list =  list(num_set)
    unic = []
    for num in numbers:
        if num not in unic:
            unic.append(num)
    return unic
listTwo = [1,1,2,3,4,4,4,5,5,5,6,6,6,7,7,7]
print(find_unique(listTwo))

# Q13 --- calculate Greatest Common Divisor(GCD) of two non-negative integers using Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(17, 7))

# Q14 -------string reverser----
def reverse_str(string):
    return string[::-1]
print((reverse_str("pit") + " from " + reverse_str("slap")))

# Q15 ---check leap year----
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
print(is_leap_year(2000))
print(22 % 6)