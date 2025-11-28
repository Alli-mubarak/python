class Dog:
    def __init__(self, name, color, age, breed):
        self.name = name
        self.color = color
        self.age = age
        self.breed = breed
    def bark(self):
        print(f'{self.name.upper()} says woof woof!')
    def introduce(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old, I am a {self.color} {self.breed} dog.')

reyna = Dog('reyna', 'brown', 3, 'labrador')
smeet = Dog('smeet', 'black', 5, 'german shepherd')

reyna.bark()
smeet.introduce()

# Attributes & methods
class Book:
    type = 'Hardcover' # class attribute
    def __init__(self, title, author, pages):
        self.title = title #instance attribute
        self.author = author #instance attribute
        self.pages = pages #instance attribute
    
    def description(self): # method
        print(f"{self.title} by {self.author}, {self.pages} pages, {self.type} book.")

book1 = Book('Lost City', 'John Doe', 200)
book1.description()

# using special methods aka (magic methods or dunder methods-- Double UNDERscore)
# the __init__ method is one such special method that initializes an object's attributes when it is created.
# we have prevoiusly used some other ones too already without knowing . e.g 
#  3 + 4 is the same as calling 3.__add__(4), also __len__(), __str__(), __sub__(), __mul__(), __truediv__()

class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart