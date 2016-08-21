import unittest
import re
import sys
from unittest  import TestCase
from collections import deque

'''
--+-
++-
--


+-++
--++
++++
'''
class Solution():
    def revert(self, cake):
        ret = ''.join(['-' if i=='+' else '+' for i in cake])
        return ret

    def panCake(self, cake):
        if cake == '+':
            return 0
        if cake == '-':
            return 1
        print cake
        if cake[-1] == '+':
            return self.panCake(cake[:-1])
        return 1 + self.panCake(self.revert(cake[:-1]))

    def solve(self, filename):
        fout = open(filename + "_output.txt", 'w')
        with open(filename, 'r') as fp:
            n = int(fp.readline().strip())
            nCase = 0
            for line in fp:
                nCase += 1
                ret = self.panCake(line.strip())
                fout.write("Case #%s: %s\n"%(nCase, ret))
        fout.close()

'''
+-+-

'''
class TestSolution(TestCase):
    def test_maxprofit(self):
        instance = Solution()
        self.assertEqual(instance.panCake("-"), 1)
        self.assertEqual(instance.panCake("-+"), 1)
        self.assertEqual(instance.panCake("+-"), 2)
        self.assertEqual(instance.panCake("-++"), 1)
        self.assertEqual(instance.panCake("+++++++-"), 2)
        
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
        suite = unittest.TestSuite([suite])  
        unittest.TextTestRunner().run(suite)
    else:
        sol = Solution()
        sol.solve(cmd)
