import sys


class CountSheep:
    def __init__(self):
        with open('/Users/zshi/Desktop/A-large.in') as f:
            content = f.readlines()
        self.num_tests = int(content[0].replace('\n',''))
        self.test_cases = []
        for i in xrange(1,self.num_tests+1):
            num = content[i].replace('\n','')
            self.test_cases.append(int(num))
        print len(self.test_cases)


    def count_sheep(self, N):
        multiplier = 1
        digits = set()
        temp = N
        if N == 0:
            return 'INSOMNIA'
        while temp < sys.maxint:
            self.store_digits(temp*multiplier,digits)
            if self.has_all_digits(digits):
                return temp*multiplier
            multiplier +=1
        return 'INSOMNIA'


    def has_all_digits(self,s):
        for i in xrange(10):
            if not i in s:
                return False
        return True

    def store_digits(self, N, s):
        temp = N
        while temp>0:
            s.add(temp%10)
            temp /= 10

    def calculate(self):
        result = []
        f = open('/Users/zshi/Desktop/code_jam.txt', 'w')
        for i in xrange(self.num_tests):
            output = self.count_sheep(self.test_cases[i])
            answer = 'Case #{0}: '.format(str(i+1)) + str(output) + '\n'
            print answer
            result.append(answer)
            f.write(answer)
        f.close()


s=CountSheep()
print s.calculate()





