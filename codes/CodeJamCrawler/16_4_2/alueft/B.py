t = int(raw_input())
for T in xrange(t):
  mx = 0
  n, k = [int(i) for i in raw_input().split()]
  p = sorted([float(i) for i in raw_input().split()])
  for i in xrange(k+1):
    V = p[:i]+p[n-k+i:]
    v = [1.0]
    for j in xrange(k):
      v2 = [0]*(len(v)+1)
      for l in xrange(j+1):
        v2[l] += v[l]*(1-V[j])
        v2[l+1] += v[l]*V[j]
      v = v2[:]
    #print i, V, v, v[k/2]
    mx = max(mx,v[k/2])
  #print n, k, p
  print "Case #{0}: {1:.10f}".format(T+1,mx)
