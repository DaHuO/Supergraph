'''
Created on 9 Apr 2016

@author: boom
'''

class Bleatrix():
    
    
    def __init__(self):
        self.number = 0
        self.seen = []
     
    def sheep_init(self, start):
        self.number = start 
        self.seen = []
          
    def sleep(self):
        
        if self.number == 0 or self.number > 1000000 or self.number < 0 : return 'INSOMNIA'
        count = 1
        number = 0
        while True:
            number = count * self.number
            if self.notice(number): break
            count = count + 1
        return number


    def notice(self, number):

        while number:
            dig = number % 10 
            if dig not in self.seen: self.seen.append(dig)
            if self.check(): return True
            number //= 10
        return False
    
    def check(self):
        
        self.seen = sorted(self.seen)
        return True if self.seen == [0,1,2,3,4,5,6,7,8,9] else False
    
def main():
    
    testfile = 'problemA.txt'
    sheep = Bleatrix()
    with open(testfile) as f:
        lineCount = 1
        next(f)
        for line in f:
            currLine = int(line.rstrip('\n'))
            sheep.sheep_init(currLine)
            print 'Case #' + str(lineCount) + ': ' + str(sheep.sleep())
            lineCount = lineCount + 1
            if lineCount > 100 : break
    
if __name__ == '__main__':
    main()