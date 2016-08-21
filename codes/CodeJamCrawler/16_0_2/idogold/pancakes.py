class Pancakes(object):
    def __init__(self, stack):
        self.stack = stack
    
    def do(self):
        counter = 0
        while not self.is_complete():
            #print self.stack
            self.flip(self.get_max_sequence())
            counter += 1
        return counter
            
    
    def get_max_sequence(self):
        for i, c in enumerate(self.stack):
            if c != self.stack[0]:
                return i
        return len(self.stack)
    
    
    def is_complete(self):
        return "-" not in self.stack
    
    def flip(self, n):
        temp_s = list(self.stack[:n][::-1])
        for i in range(len(temp_s)):
            if temp_s[i] == "-":
                temp_s[i] = "+"
            else:
                temp_s[i] = "-"
        if n != len(self.stack):
            self.stack = "".join(temp_s) + self.stack[n:]
        else:
            self.stack = "".join(temp_s)
            


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        stack = raw_input() 
        pancakes = Pancakes(stack)
        print "Case #%s: %s"% (i, pancakes.do())

if __name__ == '__main__':
    main()
        
    
    