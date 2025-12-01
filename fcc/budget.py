class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        print(f'{self.balance} added')

    def withdraw(self, amount, description=''):
        self.ledger.append({'amount': -amount, 'description': description})
        if not self.check_funds(amount):
            print('Insufficient balance')
            return False
        
        self.balance -= amount
        print(f'{amount} withdrawn\nNew Balance: {self.balance}')
        return True
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        rec_desc = f'Transfer from {destination.name}'
        sender_desc = f'Transfer to {self.name}'
        
        if not self.check_funds(amount):
            print('Transfer failed due to Insufficient funds!')
            return False

        destination.ledger.append({'amount': amount, 'description': f'Transfer from {destination.name}'})
        self.ledger.append({'amount': -amount, 'description': sender_desc})
        self.balance -= amount
        destination.balance += amount
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
    
    def __str__(self):

        num_of_asterisk = 30 - len(self.name)
        f_line = '*' * int(num_of_asterisk / 2)+self.name+'*' * int(num_of_asterisk / 2)
        trs_line = ''
        for tr in self.ledger:
            spacing = ' ' * int(23 - len(tr['description']))
            tr_line = f"{tr['description'][0:23]}{spacing}{tr['amount']:7.2f}\n"
            
            trs_line += tr_line
        total_trans = f'Total: {self.balance:.2f}'
        return f"{f_line}\n{trs_line}{total_trans}"

def create_spend_chart(categories):
    print('Percentage spent by category')
    for c in categories:
        for tr in c.ledger:
            if not tr['description'].startswith('Transfer') and tr['amount'] < 1:
                print(type(tr['amount']), tr['amount'])

cat1 = Category('purse')
cat2 = Category('wallet')
cat3 = Category('drinks')
cat4 = Category('clothing')
cat1.deposit(2000, 'from Mum')
cat2.deposit(1900, 'new deposit')
cat3.deposit(8000, 'First deposit')
cat4.deposit(7000, 'First deposit')
# print(cat1.ledger)
cat1.transfer(500, cat2)
cat2.withdraw(200.88, 'zobo purchase')
cat1.withdraw(250.25, 'crypto')
cat3.withdraw(700.55, 'Energy drink')
cat4.withdraw(950.08, 'Shirt')
# print(cat1.ledger)
# print(cat2.ledger)
# print(cat4)

create_spend_chart([cat1,cat2,cat3,cat4])
