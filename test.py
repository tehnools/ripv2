#feel free to test ideas on this file
file = open("test.txt", "rw")
f = file.read()

for lines in f.rsplit():
    print(lines)
