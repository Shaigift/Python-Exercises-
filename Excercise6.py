def tuplelist(numbers): return numbers[-1]

def thenumbers(thetuples):
    return sorted(thetuples, key=tuplelist)
print(thenumbers([(1,3), (1,5), (1,5), (1,7), (9,8)]))

