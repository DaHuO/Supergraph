def parseNumber(s):
  if 'Z' in s:
    return 0, 'ZERO'
  if 'W' in s:
    return 2, 'TWO'
  if 'U' in s:
    return 4, 'FOUR'
  if 'X' in s:
    return 6, 'SIX'
  if 'G' in s:
    return 8, 'EIGHT'
  if 'O' in s:
    return 1, 'ONE'
  if 'R' in s:
    return 3, 'THREE'
  if 'F' in s:
    return 5, 'FIVE'
  if 'V' in s:
    return 7, 'SEVEN'
  if 'N' in s:
    return 9, 'NINE'
  return None, None

def getNewString(s, d):
  result = s
  for c in d:
    result = result.replace(c, '', 1)
  return result

results = list()
cell = list()
with open('A-large.in', 'r') as f:
  testcases = int(f.readline())
  for line in f:
    while len(line) > 1:
      digit, string = parseNumber(line)
      cell.append(digit)
      line = getNewString(line, string)
    cell.sort()
    results.append(''.join(str(x) for x in cell))
    cell = list()
    print results


with open('result.txt', 'w') as f:
  for i, res in enumerate(results):
    f.write('Case #'+str(i+1)+': '+ str(res) +'\n')
