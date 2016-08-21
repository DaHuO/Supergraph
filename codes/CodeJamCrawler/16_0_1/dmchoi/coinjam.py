if __name__ == "__main__":
  T = int(raw_input())
  for t in range(T):
    digits = {}
    n = int(raw_input())
    if (n == 0):
      ans = "INSOMNIA"
    else:
      mult = 1
      while True:
        currN = tempN = n*mult
        while (tempN > 0):
          d = tempN%10
          digits[d] = True
          tempN/=10
        finished = True
        for i in range(10):
          if i not in digits:
            finished = False
        if (finished):
          ans = currN
          break
        mult += 1

    print "Case #{}: {}".format(t+1, ans)
