
class DigitCheck:
    def __init__(self,base):
        self.seen = 0
        self.base = base
        self.num  = 0
        self.check_count = 0

    def all_seen(self):
        return self.seen == 0x3ff
    
    def loop_detected(self):
        return self.base == 0 or self.check_count>1000

    def next(self):
        self.num += self.base
        self.check_count += 1
        for c in str(self.num):
            self.seen |= 1 << (ord(c)-0x30)
        return not self.all_seen() and not self.loop_detected()

    def result(self):
        if self.all_seen():
            return str(self.num)
        return 'INSOMNIA'
        

NUM_CASES = int(input())
for case_num in range(NUM_CASES):
    mult = 1
    c = DigitCheck(int(input()))
    while c.next():
        pass
    print('Case #{0:d}: {1:s}'.format(case_num+1,c.result()))

