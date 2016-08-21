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
    def frac(self, K, C, S):
        return " ".join([str(i) for i in range(1, K + 1)])

    def solve(self, filename):
        fout = open(filename + "_output.txt", 'w')
        with open(filename, 'r') as fp:
            n = int(fp.readline().strip())
            nCase = 0
            for line in fp:
                nCase += 1
                K, C, S = line.strip().split()
                K = int(K)
                C = int(C)
                S = int(S)
                ret = self.frac(K, C, S)
                fout.write("Case #%s: %s\n"%(nCase, ret))
        fout.close()

'''
select Id from Weather where Temperature > (select Temperature from Weather where 
    DateDiff(day, DateTimCol, GetDate()) = 1)
'''
class TestSolution(TestCase):
    def test_maxprofit(self):
        instance = Solution()
        self.assertEqual(len(instance.frac(2, 3, 2)), 3)
        
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
        suite = unittest.TestSuite([suite])  
        unittest.TextTestRunner().run(suite)
    else:
        sol = Solution()
        sol.solve(cmd)
