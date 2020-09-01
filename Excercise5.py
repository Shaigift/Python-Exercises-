def wordmatch(words):
    thematch = 0

    for x in words:
        if len(x) > 2 and x[0] == x[-1]:
            thematch += 1
    return thematch
print(wordmatch(['abv','ced','etf','rtr']))
