##
## Google Code Jam 2016
## Qualification Round, Apr 8
##
## Problem Title: Counting Sheep
## Author: James Hall
## Email: james.hall@infinityworks.com
##

import unittest

class TestCalculate(unittest.TestCase):

  def test_zero(self):
      self.assertEqual(calculate(0), -1)

  def test_one(self):
      self.assertEqual(calculate(1), 10)

  def test_two(self):
      self.assertEqual(calculate(2), 90)

  def test_eleven(self):
      self.assertEqual(calculate(11), 110)

  def test_1692(self):
      self.assertEqual(calculate(1692), 5076)

def calculate(params):
    n = params

    if n == 0:
        return -1
    
    digits = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" }

    count = 0
    last = n
    
    while len(digits) > 0:
        count = count + 1
        last = n * count
        for digit in str(last):
            digits.discard(digit)
        if len(digits) == 0:
            return last
        
    return last
    
if __name__ == "__main__":
##    unittest.main()
    t = int(raw_input())
    for i in xrange(1, t + 1):
        params = int(raw_input())
        result = calculate(params)
        if result < 0:
            result = "INSOMNIA"
        print "Case #{}: {}".format(i, result)
