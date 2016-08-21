def main():
  T = int(raw_input())
  for t in xrange(T):
    count = 0
    S = raw_input()
    flipAt = "-"
    for x in S[::-1]:
      if (x == flipAt):
        count += 1
        if (flipAt == "-"):
          flipAt = "+"
        else:
          flipAt = "-"
    print "Case #{}: {}".format(t+1, count)

if __name__ == "__main__":
  main()
