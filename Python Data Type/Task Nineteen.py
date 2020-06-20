def sum_thrice(x, y, z):

    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1,2,4))
print(sum_thrice(4,4,4))
