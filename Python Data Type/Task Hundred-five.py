words = input('Give words: ')
list = [x for x in words.split(",")]
print(",".join(sorted(sorted(set(list)))))
