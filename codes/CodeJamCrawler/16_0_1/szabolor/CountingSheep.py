def last(n_original, max_iter=200, is_print=False):
  n = 0
  digits = set()
  i = 0
  while (len(digits) < 10 and i < max_iter):
    n += n_original
    digits.update(set(str(n)))
    if is_print:
      print(n, digits)
    i += 1

  return (i, n)

def test(min_i, max_i, threshold, max_iter=200):
  res = []
  for i in range(min_i, max_i):
    it,_ = last(i, max_iter)
    if (it > threshold):
        res.append((i, it))
  return sorted(res, key=lambda x: -x[1])

#In [110]: test(0, 1000000, 50)
#Out[110]: [(0, 200), (125, 72), (1250, 72), (12500, 72), (125000, 72)]
# So there's only zero, which runs to infinity

def sol(n_original):
  if (n_original == 0):
    return "INSOMNIA"

  digits = set()
  n = 0
  while (len(digits) < 10):
    n += n_original
    digits.update(set(str(n)))

  return str(n)

def cgj_frame():
  CASE_N = int(input())
  for i in range(CASE_N):
    n = int(input())
    print("Case #%d: %s" % (i+1, sol(n)))

cgj_frame()