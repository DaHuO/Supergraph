def main():
  T = int(raw_input())
  for t in xrange(T):
    N = int(raw_input())
    if N == 0:
      print "Case #{}: INSOMNIA".format(t+1)
      continue
    seen = [False]*10
    num = N
    while (False in seen):
      temp = num
      seen[temp%10] = True
      temp /= 10
      while (temp > 0):
        seen[temp%10] = True
        temp /= 10
      num += N
    print "Case #{}: {}".format(t+1, num-N)

if __name__ == "__main__":
  main()
