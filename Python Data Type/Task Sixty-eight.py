def words(str):
    first_three = str[:3]
    return first_three
    if len(str) < 3:
        return str
print(words('python'))
