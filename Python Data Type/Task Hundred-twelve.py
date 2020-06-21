def change(strZ):
    char = strZ[0]
    strZ = strZ.replace(char, '$')
    strZ = char + strZ[1:]

    return strZ
print(change('together'))



