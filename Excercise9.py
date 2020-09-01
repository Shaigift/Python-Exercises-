def longerthanwords(x, str):
    words = []
    texts = str.split(" ")
    for y in texts:
        if len(y) > x:
            words.append(y)
    return words
print(longerthanwords(3, "The quick socks swallowed a python. The bear then reacted."))
