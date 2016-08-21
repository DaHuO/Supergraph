import sys

class SheepCounter(object):
    def __init__(self, N):
        self.N = N
        self.current_mul = 1
        self.current_num = N
        self.watched = [False, False, False, False, False, False, False, False, False, False]
    
    def do(self):
        while not self._is_complete():
            self.current_num = self.N * self.current_mul
            self._update_watched(self.current_num)
            self.current_mul += 1
            if self.current_mul > 100 or self.current_num == 0:
                return "INSOMNIA"
        return self.current_num
        
    def _update_watched(self, num):
        while num:
            self.watched[num%10] = True
            num /= 10
    
    def _is_complete(self):
        return False not in self.watched
    

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        num = int(raw_input())  # read a list of integers, 2 in this case
        sheep_counter = SheepCounter(num)
        print "Case #%s: %s"% (i, sheep_counter.do())

if __name__ == '__main__':
    main()

