def z(x,y):
    z = x + y
    if z in range(15, 20):
        return 20
    else:
        return z

print(z(10,7))
print(z(10, 3))
print(z(10,67))