#fixed errors in the camperbot code, love it!

n_list = '5432689997'
print(n_list[0:len(n_list)-1])
nnList = [int(d) for d in n_list]
print(nnList)



def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    try:
      main_digits = isbn[0:length - 1]
      given_check_digit = isbn[length -1]
      main_digits_list = [int(digit) for digit in main_digits]
      #main_digits_list = main_digits
    except ValueError:
        print('Invalid character was found.')
       # expected_check_digit = calculate_check_digit_10(main_digits)
    # Calculate the check digit from other digits
    else:
      if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
      else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
      if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
      else:
        print('Invalid ISBN Code.')
    

def calculate_check_digit_10(main_digits_list):
    print(main_digits_list)
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
      if(index < 9):
        digits_sum += digit * (10 - index)
        
        
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - (digits_sum % 11)
    print(f'result: {result}')
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    try:
      values = user_input.split(',')
      isbn = values[0]
      length = int(values[1])
    except IndexError:
        print('Enter comma-separated values.')
    except ValueError:
        print('Length must be a number.')
    else:
      if length == 10 or length == 13:
        validate_isbn(isbn, length)
      else:
        print('Length should be 10 or 13.')


test = '153005112X,10'
try:
  val = test.split(',')
  c = val[0]
  l = int(val[1].strip())
  length = int(l)
except IndexError:
    print('Error occurred!, there should be two values separated by a comma')
except ValueError:
    print('length should be a number!')
else:
  print(l)
  #print(c[length])
  try:
    main_char = c[0:]
    last_digit = c[length - 1]
    #main_digit = [int(d) for d in main_char]
    #main_digit = [d for d in main_char]
   #print(main_digit)
  except IndexError:
    print('Index Error occured!')
  except ValueError:
    print('Value error occurred!')
  else:
   print(last_digit)
   validate_isbn(c,l)
   
    
#main()


