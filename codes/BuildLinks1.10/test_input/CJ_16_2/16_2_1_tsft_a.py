from collections import Counter

digits = map(Counter, ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"])

def unscramble(remaining, path):
  if not remaining:
    return path
  for i, digit in enumerate(digits):
    if superset(digit, remaining):
      attempt = unscramble(remaining - digit, path + str(i))
      if attempt:
        return attempt
  return False

def superset(digit, string):
  for char in digit:
    if digit[char] > string[char]:
      return False
  return True

n = int(raw_input())
for case in range(1, n + 1):
  s = raw_input()
  nums = unscramble(Counter(s), '')
  print "Case #{0}: {1}".format(case, nums)

