import os
file = "abc.txt"
if os.path.isfile(file):
    print("File is a path file")
elif os.path.isdir(file):
    print("File is not a file path")
else:
    print("It is a special file (socket, FIFO, device file")
print()
