import unittest
import re
import sys
from unittest  import TestCase
from random import randint

'''
--+-
+-++
--++
++++
'''
class Solution():
    def get_factor(self, guess):
        for i in range(2, 10000):
            if guess % i == 0:
                return i
        return None

    def coin(self, n, m):
        low = 1 << (n - 1)
        high = 1 << n

        ret = []
        for retry in range(10000000):
            guess = randint(low, high) * 2 + 1
            guess = bin(guess)[2:]
            factors = [guess]
            for base in range(2, 11):
                real_guess = int(guess, base)
                factor = self.get_factor(real_guess)
                if factor:
                    factors.append(factor)
                else:
                    break
            if len(factors) < 10:
                continue
            ret.append(factors)
            if len(ret) >= m:
                break
        return ret

    def solve(self, filename):
        fout = open(filename + "_output.txt", 'w')
        with open(filename, 'r') as fp:
            n = int(fp.readline().strip())
            nCase = 0
            for line in fp:
                nCase += 1
                n, m = line.strip().split()
                n = int(n) - 1
                m = int(m)
                ret = self.coin(n, m)
                fout.write("Case #%s:\n"%nCase)
                for row in ret:
                    outline = " ".join([str(i) for i in row]) + "\n"
                    fout.write(outline)
        fout.close()

'''
select Id from Weather where Temperature > (select Temperature from Weather where 
    DateDiff(day, DateTimCol, GetDate()) = 1)
'''
class TestSolution(TestCase):
    def test_maxprofit(self):
        instance = Solution()
        self.assertEqual(len(instance.coin(32, 500)), 500)
        
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
        suite = unittest.TestSuite([suite])  
        unittest.TextTestRunner().run(suite)
    else:
        sol = Solution()
        sol.solve(cmd)
