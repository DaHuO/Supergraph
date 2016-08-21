def solve(i):
  if i == 0: return "INSOMNIA"

  n = int(i)
  digits = set(list(map(int,str(n))))
  while len(digits) < 10:
    n = n+i
    digits = digits | set(list(map(int,str(n))))

  return str(n)

def main():
  cases = int(input())
  for i in range(1, cases + 1):
    n = int(input())
    print("Case #{}: {}".format(i, solve(n)))

if __name__ == "__main__": main()