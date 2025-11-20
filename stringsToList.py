# new_users = "Adam Sarah John"
# new_users_list = new_users.split()
# print (new_users_list)

# site = "holo.com/index/file"
# site_list = site.split("/")
# print(site_list)

# materials = "board,meter,tester"
# mat_list = materials.split(",")
# print(mat_list)

# new_site = "dolo.home.file.net"
# new_site_list = new_site.split(".")
# print(new_site_list)
# # updating a list
# message = "We are the good ones"
# updated_message = message.replace("good", "best")
# print(updated_message)

# my_liking = "i like rice very much because rice is easy to cook"
# my_liking = my_liking.replace("rice", "beans")
# print(my_liking)
# # list comprehensions
# prices = [20, 30, 56, 20, 14, 16, 22]
# halved = []
# for price in prices:
#     half_prices = price/2
#     halved.append(half_prices)
# print(halved)

# halved_prices = [price/2 for price in prices]
# print(halved_prices)

# prices = [10, 34, 44, 28, 12, 6]
# def halve(num):
#   return  num /2
# halved = [halve(price) for price in prices]
# print(halved)
# scores = [10, 22, 7, 19, 44, 32, 18, 29]
# high_scores = [score for score in scores if score > 20]
# print(high_scores)
# low_scores = [score for score in scores if score < 20]
# print(low_scores
# )
def countVowels(words):
    letter_a = words.count("a")
    letter_e = words.count("e")
    letter_i = words.count("i")
    letter_o = words.count("o")
    letter_u = words.count("u")
    letter_A = words.count("A")
    letter_E = words.count("E")
    letter_I = words.count("I")
    letter_O = words.count("O")
    letter_U = words.count("U")
    return letter_a + letter_e + letter_i + letter_o + letter_u + letter_A + letter_E + letter_I + letter_O + letter_U

myName  = "Mubarak"
def get_name_vowels(name):
  print(f"my name is {name}, my name has {countVowels(name)} vowels")
# get_name_vowels(myName)
# get_name_vowels("Hassan")
# get_name_vowels("Alli azeezah")

# names = ["adelaide", "shazam", "cantas", "bolly"]
# def a_counter(name):
#   return name.count("a")
# a_in_names = [a_counter(name) for name in names]
# print(a_in_names)
# # sort out names that contains letter L
# l_names = [name for name in names if name.count("l")]
# print(l_names)
# # print([name for name in names if name.count(sorter())])
# print([countVowels(name) for name in names ])
def countVowels_in_name(name):
    print(f"There are {countVowels(name)} vowels in {name}")
word_input = input("I count vowels in words, enter any word: ")
countVowels_in_name(word_input)
