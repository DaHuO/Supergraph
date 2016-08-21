
inp = open('input', 'r')

frec = [ [0]*26 for i in range(10) ]
num2str = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]
# "ONE", "THREE", "FIVE", "SEVEN", "NINE"
# "ONE", "FIVE", "SEVEN", "NINE"
# "FIVE", "SEVEN", "NINE"

def rem ( f, d, ch ):
  cnt = f[ord(ch)-ord('A')]
  for i in range(26):
    f[i] -= cnt*frec[d][i]
  return str(d)*cnt

def solve(s):
  f = [0]*26
  for c in s:
    f[ord(c)-ord('A')] += 1

  r = ""
  r += rem ( f, 0, 'Z')
  r += rem ( f, 2, 'W')
  r += rem ( f, 4, 'U')
  r += rem ( f, 6, 'X')
  r += rem ( f, 8, 'G')
  r += rem ( f, 3, 'T' )
  r += rem ( f, 1, 'O' )
  r += rem ( f, 5, 'F' )
  r += rem ( f, 7, 'V' )
  r += rem ( f, 9, 'I' )

  return sorted(r)

for d in range(10):
  for c in num2str[d]:
    frec[d][ord(c)-ord('A')] += 1


ntc = int(inp.readline())
for test in range(ntc):
  r = solve(inp.readline()[:-1])
  print "Case #" + str(test+1) + ": " + ''.join(r)
