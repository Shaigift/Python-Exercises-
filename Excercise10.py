def listfunctions(listone, listtwo):
    result = False
    for x in listone:
        for y in listtwo:
            if x == y:
                result = True
                return result
print(listfunctions([1,2,4,5,55,66,66], [4,5,66,77,8,9]))
print(listfunctions([21,33,44,57,65,66], [2,3,4,5,6,7]))
