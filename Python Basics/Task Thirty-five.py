def test_number(z, a):
    if abs(z - a) == 5 or (z + a) == 5 or z == a:
        return True
    else:
        return False

print(test_number(10,8))
print(test_number(3,2))
print(test_number(2,2))