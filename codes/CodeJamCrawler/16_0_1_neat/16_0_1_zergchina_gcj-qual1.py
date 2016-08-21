import unittest
import re
import sys
from unittest  import TestCase
from collections import deque
re_num = re.compile(r'[0-9.\s]+')

class Solution():
    def countUntil(self, n):
        alphaset = set([])
        ret = "INSOMNIA"
        for i in range(1000000):
            x = i * n + n
            for a in str(x):
                alphaset.add(a)
            if len(alphaset) > 9:
                ret = x
                break
        return ret 

    def solve(self, filename):
        fout = open(filename + "_output.txt", 'w')
        with open(filename, 'r') as fp:
            n = int(fp.readline().strip())
            nCase = 0
            for line in fp:
                nCase += 1
                n = int(line.strip())
                ret = self.countUntil(n)
                fout.write("Case #%s: %s\n"%(nCase, ret))
        fout.close()

'''
select Id from Weather where Temperature > (select Temperature from Weather where 
    DateDiff(day, DateTimCol, GetDate()) = 1)
'''
class TestSolution(TestCase):
    def test_maxprofit(self):
        instance = Solution()
        for i in range(999900, 1000000):
            print instance.countUntil(i)
        self.assertEqual(instance.countUntil(0), "INSOMNIA")
        self.assertEqual(instance.countUntil(1), 10)
        self.assertEqual(instance.countUntil(2), 90)
        self.assertEqual(instance.countUntil(11), 110)
        self.assertEqual(instance.countUntil(1692), 5076)
        
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
        suite = unittest.TestSuite([suite])  
        unittest.TextTestRunner().run(suite)
    else:
        sol = Solution()
        sol.solve(cmd)
