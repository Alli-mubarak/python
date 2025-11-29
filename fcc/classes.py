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

# handling object attributes dynamically
print(getattr(reyna, 'color')) # checking if an attribute exists
print(getattr(reyna, 'colouur', 'Attribute does not exist')) # Attribute does not exist shows if the attribute is not found

# using dir() to see all attributes and methods of an object
for stuff in dir(book1):
    if not stuff.startswith('__') and not callable(getattr(book1, stuff)): #ignoring dunder methods and other methods
        print(f'{stuff} is an attribute of book1')

# using setattr() to set or modify an attribute
class Team:
    pass

team1 = Team()
setattr(team1, 'type', 'Football') # sets an attribute 'type' with value 'Football' for the team1 object

print(team1.type)
wolves_team = {
    'name': 'Wolves of Steel',
    'city': 'Detroit',
    'players': 22,
    'titles': 1,
    'describe_team': lambda self: print(f'{self.name} from {self.city} has {self.players} players and has won {self.titles} titles as a {self.type} team.')
}

for attr_name, attr_val in wolves_team.items():
    setattr(team1, attr_name, attr_val)

team1.describe_team(team1)
# using hasattr() to check if an attribute exists
print(hasattr(team1, 'Country')) # False
print(hasattr(team1, 'type')) # True

required_attrs = ['name', 'city', 'country', 'players', 'titles']
for attr in required_attrs:
    if not hasattr(team1, attr):
        print(f"ERROR: Team is missing the required attribute: '{attr}'.")
    else:
        print(f"{attr}: {getattr(team1, attr)}")

# deleting an attribute using delattr()
# delattr(team1, 'country') will raise an error since 'country attribute does not exist 
# so we need to check first using hasattr()
class Bike:
    def __init__(self, brand, model, year, buyer, seller, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.buyer = buyer
        self.seller = seller
        self.price = price
bike1 = Bike('Yamaha', 'FZ-07', 2020, 'Alice', 'Bob', 1700)
attr_to_remove = ['buyer', 'seller', 'price', 'place', 'warranty', 'color']
for attr in attr_to_remove:
    if hasattr(bike1, attr):
        delattr(bike1, attr)
        print(f"Removed attrubute: '{attr}.' ")
print('\nFinal attributes remaining:')
for attr in dir(bike1):
    if not attr.startswith("__") and not callable(getattr(bike1, attr)):
        print(f'{attr}: {getattr(bike1, attr)}')
    
