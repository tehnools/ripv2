import re

class Scanner():

    def __init__(self, filename):
        """Constructor for scanner"""
        self.filename = filename

    def scan(self):
        """Recieves file path in the form of a strings then returns each line
        @Return line.splitlines()"""
        # returns an array with full lines of strings
        print("H")
        if isinstance(self.filename, basestring):
            f = open(self.filename, "rw")
            for line in f.readlines():
                scanline(line.splitlines())
        else:
            raise("FILE ERROR: FILENAME MUST BE A STRING")

    def scanline(line):
        for token in line.split(" "):
            print(token)


def main():
    """Main executions here"""
    print("hi")
    thing = Scanner("test.txt")
    thing.scan()


if __name__ == "__main__":
    main()
