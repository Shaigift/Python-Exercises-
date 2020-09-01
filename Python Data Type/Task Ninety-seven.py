def lexicographically(y):
    return sorted(sorted(y), key=str.upper)

print(lexicographically('wvvvev44fbvc'))