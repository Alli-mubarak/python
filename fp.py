# def get_product(a, b):
#     return a * b
# def get_sum(a, b):
#     return a + b
# def get_division(a, b):
#     if a > b or a == b :
#         return a / b
#     else:
#         return "use a bigger number as the first parameter"
# def get_subtraction(a, b):
#     if a > b :
#       return a - b
#     else:
#         return "use a bigger number as the first parameter"
# num1 = 2
# num2 = 5
# num_product = get_product(num1, num2)
# print(num_product)
# print(get_product(20, 20))
# print(get_division(2, 4))
# print(get_division(30, 20))
# print(get_division(num1, num2))
# print(get_division(num2, num1))
# print(get_division(20, 20))
# print(get_subtraction(num2, num1))
# print(get_subtraction(9, 4))

def calculate(method, a, b):
    if type(a) == int and type(b) == int:
     if method == "sum":
        return a + b
     elif method == "div":
        if a > b:
            return a / b
        else:
            return "use a bigger number as the first parameter"
     elif method == "mult":
        return a * b
     elif method == "sub":
        if a > b :
          return a - b
        else:
         return "use a bigger number as the first parameter"
     else:
       return "use a method "
    else:
       return "wrong input"

sum = "sum"   
div = "div"
mult = "mult"
sub = "sub"
print(calculate(sum, 3, 5))
print(calculate(sub, 5, 6))
print(calculate(div, 9, 3))
print(calculate(mult, 3, 9))
print(calculate("log", "oo", "pp"))
print(calculate(sum, True, False))