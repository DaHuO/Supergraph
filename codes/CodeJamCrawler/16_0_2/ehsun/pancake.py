def trim(s):
  while len(s) != 0 and s[len(s)-1] == "+":
    del s[-1]
  return s

def flip(s):
  for i in range(len(s)):
    if s[i] == "+":
      s[i] = "-"
    else:
      s[i] = "+"
  return s

def _solve(s):
  if len(s) == 0: return 0

  if s[0] == "-":
    return 1 + _solve(trim(flip(s[::-1])))

  if s[0] == "+":
    i = s.index("-")
    return 1 + _solve(flip(s[:i])[::-1] + s[i:])

  return 0

def solve(s):
  return _solve(trim(list(s)))

def main():
  cases = int(input())
  for i in range(1, cases + 1):
    n = str(input())
    print("Case #{}: {}".format(i, solve(n)))

if __name__ == "__main__": main()