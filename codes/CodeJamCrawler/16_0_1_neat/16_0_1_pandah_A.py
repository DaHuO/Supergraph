def main(T, N):
  if N == 0:
    print "Case #%s: %s" % (T, "INSOMNIA")
    return
  seen = set([])
  m = 1
  while True:
    q = m * N
    map(lambda x: seen.add(x), str(q))
    if len(seen) >= 10:
      print "Case #%s: %d" % (T, q)
      return

    m += 1  

if __name__ == "__main__":
  T = int(raw_input())  
  for t in xrange(1, T+1):
    N = int(raw_input())
    main(t, N)
