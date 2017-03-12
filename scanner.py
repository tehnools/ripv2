import re

class Scanner():

    def __init__(self, filename):
        """Constructor for scanner"""
        self.filename = filename
        self.current_token_index = 0

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
                print(line)
                self.interpret_line(line.splitlines())
        else:
            raise("FILE ERROR: FILENAME MUST BE A STRING")

    def interpret_line(self, full_line):
        if full_line != None:
            line = full_line[0].split(" ")
            print(line)
            for __ in line:
                if self.current_token_index >= len(line):
                    self.current_token_index = 0
                    break
                self.switch(line[self.current_token_index], line)
                self.current_token_index += 1

    def switch(self,token,line):
        if re.match(r"router-id", token):
            self.new_router()
        elif re.match("#"+".*?", token):
            self.current_token_index = len(line)

    def new_router(self):
        print("It works")

def main():
    """Main executions here"""
    thing = Scanner("test.txt")
    thing.scan()


if __name__ == "__main__":
    main()
