class Pet:
    def __init__(self, color, name):
         self.color = color
         self.name = name
    def call(self):
         print("come here " + self.name)
    def paint(self, new_color):
         if self.color == new_color:
              print(self.name + " is already " + new_color)
         else:
           self.color = new_color
           print(self.name + " is now painted " + self.color + "!")

tango = Pet("grey", "tango")
tango.call()
tango.paint("grey")

sassy = Pet("white", "sassy")
sassy.call()
sassy.paint("white")
sassy.paint("pink")

class Wallet:
    balance = 0
    def __init__(self, name, deposit):
        self.name = name
        self.value = deposit
        self.balance += deposit
        print(f"{self.name} wallet created with initial deposit of ${self.balance}")
    def addMoney(self, amount):
        print(type(amount))
        if type(amount) == int and amount > 0:
          self.balance += amount
          print(f"Deposit of ${amount} confirmed!, balance: ${self.balance}" )

piggy = Wallet("piggy", 500)
piggy.addMoney(1)