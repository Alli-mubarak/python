class Virtual_pet:
    color = "brown"
    has_tail = True
    def bark(self):
        print("i will bark bcos i'm " + self.color )
skippy = Virtual_pet()
print(skippy.color)
print(skippy.has_tail)
skippy.bark()
class Pet :
    name = "sally"
    def scream_name(self, age):
        self.age = age
        print(f"i am {self.name}, {self.age}  years old")
new_pet = Pet()
new_pet.scream_name(3)
class Friend:
    def __init__( self, name, age, race, sex):
         self.name = name
         self.age = age
         self.race = race
         self.sex = sex
    def detail_friend(self):
          print(f"Hi, i am {self.name}, i am {self.age} years old. I am a {self.sex} {self.race}")
zeus = Friend("zeus", 29, "asian", "male")
zeus.detail_friend()

class Students:
    def __init__(self, names):
           self.names = names
    def show_names(self):
             for name in self.names:
                print(name)
ss1 = Students(["hassan", "adam", "saheed", "khaleed", "waleed", "mubarak"])
ss1.show_names()