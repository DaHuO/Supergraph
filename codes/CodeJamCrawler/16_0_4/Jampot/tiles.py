##
## Google Code Jam 2016
## Qualification Round, Apr 8
##
## Problem Title: Fractiles
## Author: James Hall
## Email: james.hall@infinityworks.com
##

import unittest

class TestCalculate(unittest.TestCase):

  def test_zero(self):
      self.assertEqual(calculate([2, 3, 2]), [1, 8])

  def test_one(self):
      self.assertEqual(calculate([1, 1, 1]), [1])

  def test_two(self):
      self.assertEqual(calculate([2, 1, 2]), [1, 2])

  def test_eleven(self):
      self.assertEqual(calculate([3, 2, 3]), [1, 5, 9])

def calculate(params):
    K, C, S = params
    k = [i for i in range(1, S+1)]
    
    if C == 1:
        return k
    
    for c in range(2, C+1):
        k = [i * K ** (c-1) + k[i] for i in range(0, len(k))]
        
    return k

if __name__ == "__main__":

##    unittest.main()
    t = int(raw_input())
    for i in xrange(1, t + 1):
        params = [int(s) for s in raw_input().split(" ")]
        result = calculate(params)
        print("Case #{}: {}".format(i, " ".join(str(x) for x in result)))
        
