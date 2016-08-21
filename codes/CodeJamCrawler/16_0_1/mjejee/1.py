size = int (raw_input())

i=0

class Numbersrecord:
    def __init__(self):
        self.x = [0,1,2,3,4,5,6,7,8,9]

    def isallcounted (self):
        return len(self.x) == 0

    def countednumber (self,number):
        try:
            self.x.remove(number)
        except:
            pass


def getcount(line):
    nr = Numbersrecord()
    startnumber = int (line)
    number = startnumber

    if number == 0:
        return 'INSOMNIA'

    while True:
        nstr = str (number)
        for element in nstr:
            nr.countednumber(int(element))
        if nr.isallcounted():
            return str(number)
        number += startnumber



while True:
    if i>=size:
        break
    i = i+1
    line = raw_input()
    print 'Case #'+ str(i) + ': ' + getcount (line)

