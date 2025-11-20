import numbers

tutor_name = 'FreeCodeCamp.org'
course_name = 'intro to Python'
student_name = 'Mubarak Alli'
random_number = 42

# data types
# integer
num = 10
num2 = -6
print(num, type(num))

# float/double
num3 = 3.56
print(num3, type(num3))

# string
greeting = 'Hello World!'
greeting2 = "Hello, python!"
greeting3 = """I love coding
in Python, lol"""
greeting4 = '''Because Python
is Awesome!'''
print(greeting, type(greeting))
print(greeting2, type(greeting2))
print(greeting3, type(greeting3))
print(greeting4, type(greeting4))

# boolean
is_learning = True
is_bored = False
print(is_learning, type(is_learning))

# complex
c_num = 5 + 9j
print(c_num, type(c_num))

# Set
my_set = {5, 4, 3, 2, 1}
print(my_set, type(my_set))

# dictionary
new_dic = {
    'name': 'Mubarak',
    'age': 25,
    'is_student': True
}
print(new_dic, type(new_dic))

# tuple
new_tuple = (9, 5, 7, 3)
print(new_tuple, type(new_tuple))

# range
new_range = range(15)
print(new_range, type(new_range))

# list
new_list = ['apple', "mango", 'cherry']
print(new_list, type(new_list))

# none
none_val = None
print(none_val, type(none_val))

print(f"{student_name} is learning {course_name} at {tutor_name}.")

# working on strings
# concatenation with +=
sentence = 'I love learning and earning at the same time. '
sentence2 = "May Allah help me"
sentence += sentence2
print(sentence)

# getting length
print(len(sentence))

# accessing character
print(sentence[10])

# neagtive indexing
print(sentence[-20])

# string slicing
print(sentence[1:20])
print(sentence[-22:])
print(sentence[0:11:1])

# checking character
print('earning' in sentence)

# string methods
print(sentence.upper())
print(sentence.lower())
new_text = '        oh my world!     '
new_text = new_text.strip()
print(new_text)
print(new_text.replace('world', 'Code'))
print(new_text.split())
new_txt = 'Apples or potatoes or mangoes or bananas'
print(new_txt.split('or'))

my_list = ['ok', 'mother', 'bye!']
print(' '.join(my_list))

print(new_text.startswith('oh'))

print(new_text.find('my'))
print(new_text.find('Code'))

print(sentence.capitalize())

print(sentence.islower())
sentence = sentence.upper()
print(sentence.isupper())

print(new_txt.title())

# working on numbers
print(2+22)
print(200+22.65)
print(87 % 7) #modulus
print(20 - 12.5)

print(87 // 7) #floor division
print(11 // 2)
print(200 // 1.8)


print(2 ** 5) #raised to power

print(type(float(9)))
print(type(int(9.98)), int(9.98))
print(type(int('23')))

print(round(3.8756))
print(round(3.235))

print(abs(-29))

print(bin(56))
print(oct(56))
print(hex(56))

print(pow(29,5)) #29 raised to power 5

# augmented assignment operators
count = 10
count +=15
print(count)

count -=5
print(count)

count *=5
print(count)

count /=2
print(count)

count //=15
print(count)

count*=20
count %= 7
print(count)

count **=3
print(count)

# augmented operation on strings
txt = 'hola'
txt += ' amigo. '
print(txt)

txt *= 3
print(txt)

# functions 

def div(a, b):
    if (a % b == 0):
        return f"{a // b} remainder 0"
    else:
        return f"{a // b} remainder {a % b}"
    
print(div(85, 70))
# print(div())

# scopes - LEGB rule ( Local, Enclosing, Global, Built-in)
def outer():
    msg = 'okay sir' #local scope

    def inner(): #enclosing scope
        print(msg)
        global  res #global variable
        res = 'on it'

    inner()
    # print(res)

outer()
print(res)

# changing a global variable
def change_txt():
    global txt #allows modification for a global variable
    txt = 'Hola, this is changed now!'
    return txt

print(change_txt())

# using conditionals
child_age = 19
canDrive_well = True

def canDrive():
    if (child_age >= 18 and not canDrive_well):
      return 'You are old enough to drive but you need more practice'
    elif (canDrive_well and child_age >= 18):
        return 'You are good to go!'
    else:
      return 'you are too young!'

print(canDrive())
# boolean operators are " and, or, not "

# inp = input('What is your name?: ')
# print(f'Hello, {inp}!')

def say_hello():
    name = input('What is your name? ')
    return 'Hello ' + name

def uppercase_decorator(func):
    def wrapper():
        original_func = func()
        modified_func = original_func.upper()
        return modified_func
    return wrapper

say_hello_res = uppercase_decorator(say_hello)

# print(say_hello_res())
def greet():
    pass

print(greet())

# List , Tuples & Range
new_list = ['apcot', 'mannot', "kolion"]
print(new_list[0])
print(new_list[-1]) #negative indexing

# creating list from string
dev = 'Johnny'
print(list(dev))
# getting length of list
print(len(new_list))

new_list[1] = 'Maukot' #modifying item
print(new_list)

# new_list[3] = 'bantanks' -- returns error
del new_list[0] # deleting item
print(new_list)

# checking for a value in a list
toDo = ['eat', 'code', 'exercise', 'sleep', 'repeat']
print('sleep' in toDo)

# nested lists
new_lang = ['Rust', 'Go', ["Nodejs", 'Reactjs', 'Angularjs', "JavaScript"]]
print(new_lang[2][3])

# list unpacking
user = ['Smith', 20, 'Designer', 'Germany']
name, age, profession, country = user
print(name, age, country)

user2 = ['Jane', 30, 'Developer', 'India']
name2,*rest = user2
print(name2, rest)

# list slicing
print(toDo[1:4])
nums = [1,2,3,4,5,6,7,8,9]
print(nums[1::2]) #step value of 2 - showing only even numbers
print(nums[::-1]) #reversing a list

# LIST METHODS
toDo.append('read') # adding item to the end
new_todo_list = ['copy code', 'paste code', 'test code']
toDo.append(new_todo_list)
print(toDo)

exercise_list = ['run', 'swim', 'jog']
toDo.extend(exercise_list) # adding multiple items to the end - merging two lists
print(toDo)

toDo.insert(0, 'wake up') # inserting item at a specific index
print(toDo)

nums.remove(5) # removing item by value - removes first occurrence
print(nums)

toDo.pop() # removing last item
toDo.pop(7) # removing item at specific index i.e the list previously added
print(toDo)

nums.clear() #emptying a list
print(nums)

nums = [12, 34, 10, 2, 3, 67, 90, 99, 76, 55, 29, 20, 33, 44, 18]
nums.sort() #sorting a list in ascending order
print(nums)
nums.sort(reverse=True) #sorting a list in descending order
print(nums)

# using sorted()
nums2 = [2, 66, 1, 87, 20, 55, 55, 12, 44, 100]
sorted_num = sorted(nums2)
print(sorted_num)

toDo.reverse() # reversing a list
print(toDo)

print(toDo.index('code')) # getting index of an item
# print(toDo.index('coders')) # returns error because item is missing

# TUPLE
new_tuple = ('go', 'come', 'sit', 'eat', 12)
# new_tuple[0] = 'run' will return error because tuples are immutable
print(new_tuple[0], new_tuple[-1]) #allows negative indexing
# print(new_tuple[6]) # returns index error

some_text = 'i love coding!'
print(tuple(some_text)) # using tuple() method to create a tuple
print(12 in new_tuple) # checking for a value with 'in'

# we can unpack tuples like lists too
f_com, s_com, t_com, ft_com, age = new_tuple
print(t_com, age)

# or use asterisk operator '*'
h_tuple = ('Adam', 'Asian', 'White', 45, 'single')
h_name, *other_info = h_tuple
print(h_name)
print(other_info)

# WE USE LISTS WHEN WE NEED TO CHANGE ELEMENTS, WE USE TUPLES WHEN THERE WILL NOT BE FURTHER CHANGES 

# tuples method
some_tuple = (1, 2, 3, 4, 5,2,2, 1,3)
print(some_tuple.count(2)) # returns the count of the passed value and 0 if not found
print(h_tuple.index('single')) # returns the index of the passed value and 'valueError' if not found
tuple_2 = ("oh", "hi", "hey",'oh', "ouch", "yeh", "ooh", "oh", "aich", "oh")
print(tuple_2.index('oh', 4)) # returns the index of the passed value starting from the 2nd index
print(tuple_2.index('oh', 2, 4)) # returns the index of the passed value starting from 2 and ending at 4

some_tuple2 = sorted(some_tuple) # returns the tuple elements in ascending order
# we can customize the sorting behaviour with 'key' and 'reverse' arguments
some_tuple3 = sorted(some_tuple, reverse=True ) # returns the tuple elmenents in ascending order
some_langs = ('Hausa', 'Arabic', 'Zulu', 'French', 'Portuguese', 'Hebrew', 'Japanese')
some_langs2 = sorted(some_langs, key=len)
print(some_tuple2)
print(some_tuple3)
print(some_langs2)

# loops
# for loops
new_lang = ['Go', 'Rust', 'Java', 'CSS', 'Python', 'C++']
lang2 = 'Javascript'
for s in new_lang: #looping through a list
    print(s)

for char in lang2: # looping through a string
    print(char)

# while loops
sec_num = 5
guess = 0

while guess != sec_num:
    guess = int(input('Guess the number (1-5): '))
    if guess != sec_num:
        print('Wrong! Try again.')

print('You got it!')

# nested loops
cat = ['Vegetable', 'Fruits']
foods = ['Apple', 'Banana', 'Cherry']

for c in cat:
    for f in foods:
        print(c, f)

# using break statements with conditionals
for l in new_lang:
    if l == 'Python':
        break
    print(l)
# the print out stops if 'Python' is found and skips the remaining ones after

# using continue statement
for l in new_lang:
    if l == 'CSSl':
        continue
    print(l)

# the print out skips  'CSS' if found and continues to the end

# using if and else with break statement
words = ['sky', 'apple', 'blue', 'why', 'dry', 'rhythm', 'orange', 'dark']
for word in words:
    for l in word:
        if l.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{l}' ")
            break
        else:
            print(f"'{word}' has no vowels")