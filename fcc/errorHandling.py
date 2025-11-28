# try:
#     result = 10 / 0
# except ZeroDivisionError :
#     print('Error: Division by sero is not allowed!')

def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError :
        return 'Error: Division by zero is not allowed!'
    except TypeError:
        return 'Error: Invalid input type. Please provide numbers only.'
    else:
        return result
    finally:
        print('Execution completed.')
# print(div(25, 9))

# using raise keyword
def check_eligibility(age):
    if isinstance(age, int) and age < 18:
        raise ValueError('Age must be at least 18 to be eligible.')
    if not isinstance(age, int):
        raise TypeError('Age must be an integer value.')
    return f'An Individual of {age} years old is eligible to vote.'

try:
    print(check_eligibility(2))
except ValueError as ve:
    print(f'Error: {ve}')
except TypeError as te:
    print(f'Error: {te}')

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')

#  using custom exceptions classes
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 250)
    print(f'Withdrawal successful. New balance: ${new_balance}')
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')

# raising from None
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

# config = parse_config('config.txt')

#You can also raise exceptions conditionally using assert statements, which are essentially shorthand for raise with AssertionError:

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')