n=input()

def shift_bit_length(x):
    return ((x).bit_length()) - 1

def compute(b, m):
  if 2**(b-2) < m:
    print 'IMPOSSIBLE'
    return
  print 'POSSIBLE'
  matrix = [[0 for _ in range(b)] for __ in range(b)]
  if m > 0:
    startX, startY = b - 2, b - 1
    fill = shift_bit_length(m)
    while fill >= 0:
      posY = startY
      while posY < b:
        matrix[startX][posY] = 1
        posY += 1
      fill -= 1
      startX -= 1
      startY -= 1
    while startX >= 0:
      matrix[startX][startY] = 1
      startX -= 1
      startY -= 1
  last = bin(m)[3:]+'0'
  for idx in xrange(len(last)):
    if last[idx] == '1':
      matrix[0][b - len(last) + idx] = 1
  print '\n'.join(''.join(map(str, ma)) for ma in matrix)

for x in xrange(n):
  b, m = map(int, raw_input().split(' '))
  print 'Case #'+str(x+1)+':',
  compute(b, m)