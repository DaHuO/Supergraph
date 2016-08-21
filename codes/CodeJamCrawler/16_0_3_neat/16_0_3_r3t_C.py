def is_prime(n):
  i = 2
  while i*i <= n:
    if n % i == 0:
      return i
    i += 1
  return -1

def main():
  test = int(raw_input())
  N, J = map(int, raw_input().split())
  cnt = 0

  print 'Case #%d:' % test
  for i in xrange(2**N):
    b = bin(i)[2:]
    if b[0] == '1' and b[-1] == '1' and len(b) == N:
      n = int(b)
      st = {}
      for j in xrange(2, 11):
        div = is_prime(int(str(n), j))
        if div == -1:
          break
        st[j] = div
      if len(st) == 9:
        print n, ' '.join([str(elem[1]) for elem in st.items()])
        #print n, st
        cnt += 1
      if cnt >= J:
        break

if __name__ == "__main__":
  main()
