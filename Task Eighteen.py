def near_thousands(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousands(1000))
