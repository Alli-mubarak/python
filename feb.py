class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("hi")
    def introduce(self):
        print(f"hi, my name is {self.name} and i am {self.age} years old")
sam = Person("sam", 23)
sam.greet()
sam.introduce()
# inheritance
class Father(Person):
    def greet(self):
        print("i am the father here!")
bob = Father("bob", 45)
bob.greet()

class Human:
    def cry(self):
        print("haaaa")
class Baby(Human):
    def cry(self):
        print("waaauun")
ted = Human()
billy = Baby()
ted.cry()
billy.cry()
