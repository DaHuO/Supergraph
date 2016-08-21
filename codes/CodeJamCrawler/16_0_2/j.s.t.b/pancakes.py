#!/usr/bin/env python3

BLANK = '-'
HAPPY = '+'
ALLOWED_STATES = set([BLANK, HAPPY])

FILENAME = "B-large"

class Stack():

    def __init__(self, pancakestring):
        assert set(pancakestring).issubset(ALLOWED_STATES)
        self.pancakes = list(pancakestring)
        self.number_of_operations = 0

    def __repr__(self):
        return "{} ({} pancakes), {} operations".format(
                    ''.join(self.pancakes),
                    len(self),
                    self.number_of_operations)
        
    def __len__(self):
        return len(self.pancakes)
        
    def __bool__(self):
        return bool(self.pancakes)
        
    def flip(self, number_of_pancakes):
        if number_of_pancakes < 1:
            raise ValueError("The stack is empty")
        assert number_of_pancakes <= len(self)
        
        substack = self.pancakes[0:number_of_pancakes]
        remaining = self.pancakes[number_of_pancakes:]
        flipped = [BLANK if x==HAPPY else HAPPY for x in list(reversed(substack))]
        assert len(flipped) + len(remaining) == len(self)
        
        self.pancakes = flipped + remaining
        self.number_of_operations += 1
        
    def shorten(self):
        out = []
        for i, pancake in enumerate(self.pancakes):
            if not i:
                out.append(pancake)
            else:
                if pancake != out[-1]:
                    out.append(pancake)
        
        if out:
            if out[-1] == HAPPY:
                out = out[:-1]
        self.pancakes = out
        
    def flip_and_shorten(self, number_of_pancakes):
        self.flip(number_of_pancakes)
        self.shorten()
    
    def shorten_flip_all_and_shorten(self):
        self.shorten()
        self.flip_and_shorten(len(self))
        
    def flip_first_and_shorten(self):
        self.flip_and_shorten(1)
    
    def handle(self):
        print(self)
        self.shorten()
        print(self)
        while self:
            if self.pancakes[0] == BLANK:
                pancakes.shorten_flip_all_and_shorten()
            else:
                pancakes.flip_first_and_shorten()
            print(self)
    
    def shorten_and_calculate_number_of_required_operations(self):
        self.shorten()
        return len(self)
    
    
with open(FILENAME + ".in", 'r') as inputfile:
    lines = inputfile.readlines()

with open(FILENAME + ".out", 'w') as outputfile:
    number_of_tests = 0
    for linenumber, line in enumerate(lines):
        if linenumber == 0:
            number_of_tests = int(line.strip())
            print("There are {} tests".format(number_of_tests))
        elif linenumber > number_of_tests:
            break
        else:
            casenumber = linenumber
            pancakestring = line.strip()
            pancakes = Stack(pancakestring)
            print(pancakes)
            operations = pancakes.shorten_and_calculate_number_of_required_operations()

            answer = "Case #{}: {}\n".format(casenumber, operations)
            print(answer)
            outputfile.write(answer)
