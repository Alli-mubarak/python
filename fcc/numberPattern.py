def number_pattern(n):
    is_n_integer = isinstance(n, int)
    if not is_n_integer:
        return 'Argument must be an integer value.'
    elif is_n_integer and n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        num_string = ''
        for num in range(n):
            num_string+=str(num+1) + ' '
        return num_string.strip()

print(number_pattern(0.9))
print(number_pattern(9))
print(number_pattern(2.5))
print(number_pattern(-9))
print(number_pattern(-8.9))