from collections import defaultdict
letters = \
  {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
  }

T = int(input())
for t in range(T):
  d = defaultdict(int)
  ans = ''
  S = input()
  for s in S:
    d[s] += 1
  if 'Z' in d:
    count = d['Z']
    for letter in letters[0]:
      d[letter] -= count
    ans += '0'*count
  if 'W' in d:
    count = d['W']
    for letter in letters[2]:
      d[letter] -= count
    ans += '2'*count
  if 'U' in d:
    count = d['U']
    for letter in letters[4]:
      d[letter] -= count
    ans += '4'*count
  if 'X' in d:
    count = d['X']
    for letter in letters[6]:
      d[letter] -= count
    ans += '6'*count
  if 'G' in d:
    count = d['G']
    for letter in letters[8]:
      d[letter] -= count
    ans += '8'*count
  if 'O' in d:
    count = d['O']
    for letter in letters[1]:
      d[letter] -= count
    ans += '1'*count
  if 'H' in d:
    count = d['H']
    for letter in letters[3]:
      d[letter] -= count
    ans += '3'*count
  if 'F' in d:
    count = d['F']
    for letter in letters[5]:
      d[letter] -= count
    ans += '5'*count
  if 'V' in d:
    count = d['V']
    for letter in letters[7]:
      d[letter] -= count
    ans += '7'*count
  ans += '9' * d['I']

  print('Case #{}: {}'.format(t+1, ''.join(sorted(ans))))
