def main():
  T = int(raw_input())
  for t in xrange(T):
    ans = ""
    S = raw_input()
    for s in S:
      if (len(ans) > 0 and s < ans[0]):
        ans = ans + s
      else:
        ans = s + ans
    print "Case #{}: {}".format(t+1, ans)

if __name__ == "__main__":
  main()
