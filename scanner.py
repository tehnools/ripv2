import re
import sys

class Scanner():

    def __init__(self, filename):
        """Constructor for scanner
        @var filename, current_token_index
        @Return None"""
        self.filename = filename
        self.current_token_index = 0
        self.line_index = 0

    def scan(self):
        """Recieves file path in the form of a strings
        then executes interpret_line
        @var f,
        @funct isinstance, readlines, interpret_line
        @Return None"""
        if isinstance(self.filename, basestring):
            f = open(self.filename, "rw")
            for line in f.readlines():
                self.line_index += 1
                self.interpret_line(line.splitlines())
        else:
            sys.exit("FILENAME MUST BE A STRING")

    def interpret_line(self, full_line):
        """ Recieves a line at a time splits the lines by space and calls switch
        to check the current token
        @Return None"""
        if full_line != None:
            self.current_token_index = 0 #resets once loops to new line
            line = full_line[0].split(" ")
            for __ in line:
                if self.current_token_index >= len(line):
                    break
                self.switch(line[self.current_token_index], line)
                self.current_token_index += 1

    def switch(self,token,line):
        """Checks for all the statically typed cases in if statements."""
        if re.match(r"router-id", token):
            self.new_router(line)
        elif re.match("#"+".*?", token):
            self.current_token_index = len(line)
        else:
            sys.exit("LINE " + str(self.line_index) +
            " : Does not follow proper Syntax at... " + line[0])

    def new_router(self, line):
        """Creates New instance of router checks if next token is an integer
        @Return None"""
        if re.match(r"\d", line[self.current_token_index + 1]):
            self.current_token_index += 1
        else:
            sys.exit("LINE " + str(self.line_index) +
            " : Integer must follow router-id")

def main():
    """Main executions here"""
    thing = Scanner("test.txt")
    thing.scan()


if __name__ == "__main__":
    main()
