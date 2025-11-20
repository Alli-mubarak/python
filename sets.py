foods = {"rice", "yam", "beans"}
# print(foods)
tracks = ["load me up", "good for two", "nicer", "open and free", "good for two"]
# print(tracks)
# convert the list to sets by eliminating duplicates
tracks_set = set(tracks)
# print(tracks_set)
# adding values to the foods set
foods.add("tomatoes")
foods.add("noodles")
foods.add("rice")
# print(foods)
# checking for values in set
has_fish = "fish" in foods
has_beans = "beans" in foods
# print(has_beans)
# print(has_fish)
# using loops
# for food in foods:
#     print("available items: " + food)
# # removing values
# foods.remove("tomatoes")
# # print(foods)
# if "garri" in foods:
#   foods.remove("garri")
# else:  
#    print(foods)

# subsets
urgent_foods = {"noodles", "rice"}
print(urgent_foods.issubset(foods))

# joining sets together
my_friends = {'adam', 'shade', 'amaka', 'jerry'}
your_friends = {'titi', 'zeus', 'terry', 'adam'}
all_friends = my_friends.union(your_friends)
# finding common values
common_friends = my_friends.intersection(your_friends) 
# finding differences
only_my_friends = my_friends.difference(your_friends)
only_your_friends = your_friends.difference(my_friends)
# 

# modules
import statistics, math
scores = [10, 22, 14, 6, 2, 20]
# print(statistics.mean(scores))
# print(math.pi)
# print(help(math))
# print(help(statistics))
from statistics import mean
print(mean(scores))

# Errors
# print(mama)
# print(scores[11])
# print(200/0)
# print("22" + 22)
# using raise keyword
# days = 5
# if days < 6:
#   raise ValueError(" days not enough")
# using try and except
numba  = 80
try:
  new_number = 23 + numba
except:
  raise TypeError("invalid number!")
  # pass
else:
  print(new_number)
finally:
  print("try again fren!")