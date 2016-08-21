__author__ = 'pavlovick'
T_MAX = 100

class sleepCount:
        def __init__(self, a):
                self.a = a
                self.allDigit = '0123456789'
                self.count = 0
                self.dictApply(a)
                self.result = self.sleepCount(a)

        def dictApply(self, a):
                for digit in str(a):
                        if digit in self.allDigit:
                                self.allDigit = self.allDigit.replace(digit,'')


        def sleepCount(self, a):
                while self.count < T_MAX and self.allDigit != '' :
                        a= a + self.a
                        self.dictApply(a)
                        self.count += 1
                if self.count < T_MAX:
                        return a
                else:
                        return 'INSOMNIA'


solution = open('bigSolution.txt', 'w')
with open('test.txt') as f:
    N= int(f.readline())
    count = 1
    for line in f:
             sleep = sleepCount(int(line))
             newLine = 'Case #'+ str(count) +': '+ str(sleep.result) +'\n'
             solution.write(newLine)
             count +=1
