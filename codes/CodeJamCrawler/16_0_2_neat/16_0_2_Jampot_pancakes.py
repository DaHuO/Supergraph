##
## Google Code Jam 2016
## Qualification Round, Apr 8
##
## Problem Title: Revenge of the Pancakes
## Author: James Hall
## Email: james.hall@infinityworks.com
##

import unittest

class TestCalculate(unittest.TestCase):

  def test_minus(self):
      self.assertEqual(calculate(["-"]), 1)

  def test_minus_plus(self):
      self.assertEqual(calculate(["-", "+"]), 1)

  def test_plus_minus(self):
      self.assertEqual(calculate(["+", "-"]), 2)

  def test_three_plus(self):
      self.assertEqual(calculate(["+", "+", "+"]), 0)

  def test_m_m_p_m(self):
      self.assertEqual(calculate(["-", "-", "+", "-"]), 3)

def calculate(params):
    pancakes = params

    count = 0
    current = pancakes[0]

    for i in range(1, len(pancakes)):
        if pancakes[i] != current:
            count += 1
            current = pancakes[i]

    if current == "-":
      count += 1

    return count
    
if __name__ == "__main__":
##    unittest.main()
    t = int(raw_input())
    for i in range(1, t + 1):
        params = [s for s in raw_input()]
        result = calculate(params)
        print "Case #{}: {}".format(i, result)
