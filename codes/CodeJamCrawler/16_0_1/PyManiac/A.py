def call(N):
  if N == 0:
    return "INSOMNIA"
  val = set()
  i = 0
  q = 0
  while (i < 10000):
    i += 1
    q += N
    val.update(list(str(q)))
    if {'0','1','2','3','4','5','6','7','8','9'}.difference(val) == set():
      return q
  return "INSOMNIA"





fp = open('a.in' , 'r')
fout = open('a.out' , 'w+')

for i in range(int(fp.readline())):
  N = int(fp.readline())
  ans = call(N)
  fout.writelines("Case #" + str(i+1) + ": " + str(ans) + '\n')

fp.close()
fout.close()

  


