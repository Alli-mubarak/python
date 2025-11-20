# # # students = ["alex","john","reynald"]
# # # def list_students(name):
# # #     print("All students are:")
# # #     for items in name:
# # #         print(items)
# # # list_students(students)
# # # for i in range(10):
# # #     print(i + 1)

# # # def helper(a, b, counter):
# # #     if counter == 0:
# # #       return 0
# # #     return a + helper(a, b, counter - 1)

# # # def multiply(a, b):
# # #     if (a == 0 or b == 0):
# # #         return 0
# # #     return helper(a, b, b)



# # # print(multiply(2, 2))
# # # print(multiply(6, 9))
# # # print(multiply(4, 2))
# # # print(multiply(21, 2))
# # # print(multiply(2, 20))

# # first_task = "home work"
# # first_task = "wash plates"
# # second_task = "sweep"
# # third_task = "feed chicken"
# # print(first_task, second_task, third_task)
# # priority_task = second_task
# # print(priority_task)


# my_age = 24
# my_name = "Mubarak"
# is_adult = True
# about_me = f"My name is {my_name} , i am  {my_age} years old"


# is_equal = 100 == 120
# is_equal = 10 == 10
# # print(is_equal)
# # print(my_age == 24)
# # print(11 != 22)
# # print(20 > 15)
# # print(100 != 100)

# usman_age = 11
# azeezah_age = 8

# def can_cook(age):
#     if age > 10:
#         return "You can cook"
#     else:
#         return "You cannot cook"
# # print(can_cook(azeezah_age))

# def can_drive(age):
#     if age > 18:
#         return "You may drive"
#     else:
#         return "Do not go near the steering!"
#     return age
# # print(can_drive(my_age))
# # print(can_drive(azeezah_age))
# # print(can_drive(usman_age))
# # print(type(222.2))
# # print(type(22))
# # print(type('mummy'))
# # print(type(False))
# # print(int(34.67))
# # print(float(43))
# # # print(3/2)
# # name = input("What is your name: ")
# # print(f"Welcome here, {name}")
# # age = input("How old are you: ")
# # brother_age = input("How old is your older brother: ")
# # print(f" You will be {int(age) + 2} years old in 2026")
# # print(f" You are {int(brother_age)-int(age)} years younger than your elder brother")
# number = 2+8
# if(number > 20):
#     print("Good")
# elif(number < 5):
#     print("bad")
# else:
#     print("moderate")
# print("figure")
# # print(bool(67))
# # print(bool(0))
# def can_discuss(age,has_sense):
#     if(age > 12 and has_sense):
#         print("You can engage")
#     elif(age > 12 or has_sense):
#         print("let us hear you out")
#     else:
#         print("shut up fren!")
# person_age = 22
# person_has_sense = False
# # can_discuss(person_age, person_has_sense)
# my_bal = 100
# my_bal = my_bal + 200
# my_bal += 500
# my_bal -= 22
# is_broke = 1
# while is_broke < 5:
#   print(my_bal)
#   is_broke += 1
# for i in range(5):
#     print(f"I love Python {i + 1} times")
# print("I love python for life")

# cars = ["Ferrari", "Mazda", "Bugatti", "Toyota"]
# for models in cars:
#     print(f"{models} is a popular brand")
# x, y, z = 3, 5, 6
# print(x,"+", y, "+", z, "=", x +y+ z)

to_do = ["read", "shower", "cook", "game"]
to_do[1] = "race"
to_do.pop()
to_do.append("sweep")
to_do.insert(1, "dance")
to_do.pop(1)
print(to_do)
scores = [1,45,5.4,21,4.98,-7,91,2,54,2.7,-3.4]
scores.sort()
total_scores = sum(scores)
print(scores)
print(max(scores))
print(min(scores))
print(total_scores)