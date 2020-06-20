def check_integer_type(x, y):
    if isinstance(x , int) and isinstance(y, int):
        return (x + y)
    else:
        return print('Number must be an integer')

print(check_integer_type(14,13))
print(check_integer_type(14.5, 7))

