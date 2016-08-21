import fileinput

inputFile = fileinput.input();

#inputFile = f = open('sample.txt', 'r')
t = int(inputFile.readline())


def findMinMove(st):
  if st[-1] == '\n':
      st = st[:-1]
  st += '+'
  prev = st[0]
  cnt = 0
  for ch in st[1:]:
      if ch != prev:
          prev = ch
          cnt += 1
  return cnt






for i in range(t):
    st = inputFile.readline()
    print("Case #" + str(i + 1) + ": " + str(findMinMove(st)))




