String_words = 'Once upon a time Jack and Jill went up the Hill. On the hill jack fell down and broke his crown'
word_list = String_words.split()
word_freq = [word_list.count(n) for n in String_words]

print(f'The Strings are{String_words}')
print(f'The Lists are {word_list}')
print(f'The pairs; words and frequencies are {str(list(zip(word_list, word_freq)))}')

