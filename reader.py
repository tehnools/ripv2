import re

def readpy(filename):
    if isinstance(filename, basestring):
        f = open(filename, "rw")
        print(f.readlines())

    else:
        print("ERROR: FILENAME MUST BE A STRING")

readpy("test.txt")
