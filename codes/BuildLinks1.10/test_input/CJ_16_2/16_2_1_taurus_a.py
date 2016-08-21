zero = "ZERO"
one = "ONE"
two = "TWO"
three = "THREE"
four = "FOUR"
five = "FIVE"
six = "SIX"
seven = "SEVEN"
eight = "EIGHT"
nine = "NINE"

def main():
  testcases = int(input())
  for caseNr in range(1, testcases+1):
    s = input()
    # l,u = map(int, input().split())
    #board = input() # legge una riga e crea una lista
    #board = [input() for i in range(4)] #legge 4 righe e crea una lista di liste
    #pattern = [list(map(int, input().split())) for i in range(N)] #
    print("Case #%i: %s" % (caseNr, solve(s)))

def solve(s):  
  d = dict()
  for c in s:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1
      
  zeros = countChar('Z', d)
  twos = countChar('W', d)
  fours = countChar('U', d)
  sixes = countChar('X', d)
  eights = countChar('G', d)
      
  res = [0 for i in range(0,10)]
  res[0] = zeros
  res[2] = twos
  res[4] = fours
  res[6] = sixes
  res[8] = eights
  
  d = removeWord(zero, zeros, d)
  d = removeWord(two, twos, d)
  d = removeWord(four, fours, d)
  d = removeWord(six, sixes, d)
  d = removeWord(eight, eights, d)
  
  # print(d)
  
  # 2nd
  
  ones = countChar('O', d)
  threes = countChar('H', d)
  fives = countChar('F', d)
  sevens = countChar('S', d)
      
  res[1] = ones
  res[3] = threes
  res[5] = fives
  res[7] = sevens
  
  d = removeWord(one, ones, d)
  d = removeWord(three, threes, d)
  d = removeWord(five, fives, d)
  d = removeWord(seven, sevens, d)
  
  # print(d)
  
  # 3rd
  
  # print(d)
  
  nines = countChar('E', d)
      
  res[9] = nines
  
  # print(res)
  
  final = ""
  for i in range(0, 10):
    v = res[i]
    for j in range(0, v):
      final += str(i)
      
  return final
      
def countChar(c, d):
  if c in d:
    return d[c]
  else:
    return 0
    
def removeWord(s, n, d):
  if n == 0:
    return d
  
  for c in s:
    d[c] -= n
  return d


if __name__ == "__main__":
  main()
