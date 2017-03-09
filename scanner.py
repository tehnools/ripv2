import re

class Scanner():

    def __init__(self, filename):
        """Constructor for scanner"""
        self.filename = filename
        self.line_count = 0

    # def scanline(self, line):
    #     for token in line[0].split(" "):
    #          return(token)

    def scan(self):
        """Recieves file path in the form of a strings then returns each line
        @Return line.splitlines()"""
        # returns an array with full lines of strings
        if isinstance(self.filename, basestring):
            f = open(self.filename, "rw")
            for line in f.readlines():
                self.interpret_line(line.splitlines())
        else:
            raise("FILE ERROR: FILENAME MUST BE A STRING")

    def interpret_line(self, full_line):
        if full_line != None:
            line = full_line[0].split(" ")
            current_token_index = 0

    def switch(self,token):
        {
        'router-id': new_router
        }.get(token, 100)

    def new_router(self):
        print("It works")

def main():
    """Main executions here"""
    print("main executed")
    thing = Scanner("test.txt")
    thing.scan()


if __name__ == "__main__":
    main()
