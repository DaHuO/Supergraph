def solve(n):
  res = ''
  zeros = n.count('Z')
  twos = n.count('W')
  fours = n.count('U')
  sixs = n.count('X')
  eights = n.count('G')
  ones = (n.count('O')-zeros-twos-n.count('U'))
  threes = (n.count('H')-eights)
  sevens = (n.count('S')-sixs)
  fives = (n.count('F')-fours)
  res+='0'*zeros
  res+='1'*ones
  res+='2'*twos
  res+='3'*threes
  res+='4'*fours
  res+='5'*fives
  res+='6'*sixs
  res+='7'*sevens
  res+='8'*eights
  res+='9'*int((n.count('N')-ones-sevens)/2)
  return res

# input() reads a string line, stripping the '\n' at the end.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  # read a list of integers, 2 in this case
  n = input()
  n = solve(n)
  print("Case #{}: {}".format(i, n))

'''
# input() reads a string line, stripping the \n at the end.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  # read a list of integers, 2 in this case
  n, m = [int(s) for s in input().split(" ")]
  print("Case #{}: {} {}".format(i, n, m))
'''
