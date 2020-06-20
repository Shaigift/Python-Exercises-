testing_string = "dvcevervecadcfvs"
all_freq = {}
for i in testing_string:
    if i in all_freq:
        all_freq[i] +=1
    else:
         all_freq[i]=1
print(f"Count of all the characters in 'testing_string' is : {all_freq}")

