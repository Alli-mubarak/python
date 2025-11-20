users = ["Tony", "Tina", "Tom"]
last = users[-1]
first = users[-3]
print(last)
print(first)
users[-2] = "Timothy"
print(users)

users_tuple = ("ada", "bola", "paul")
print(users_tuple[-2])
print(users_tuple[-3])
data = ["name", "age", "hobby", "adddress"]
del data[-1]
print(data)
del users_tuple
# print(users_tuple)
dic = {'name': 'John', 'age': 44, 'Best food': 'Pizza', 'race': 'American'}
del dic['Best food']
print(dic)
ingredients = ["eggs", "flour", "sugar", "salt"]
print(ingredients[2:0])
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(alphabets[ : : 2])
print(alphabets[::-2])
print(ingredients[:-2])
