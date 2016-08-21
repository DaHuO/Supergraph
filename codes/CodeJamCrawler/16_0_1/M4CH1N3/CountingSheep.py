T = int(input().strip())
file = open('output.txt', 'w')
for j in range(T):
  change = set()
  repeat = 0
  N = input().strip()

  seen = [False]*10
  i = 1
  while True:
    temp = str(int(N)*i)
    if temp not in change:
      change.update(temp)
    else:
      repeat += 1
    for x in temp:
      seen[int(x)] = True
    if all(seen):
      ans = int(N)*i
      break
    i += 1
    if repeat > 10:
      ans = 'INSOMNIA'
      break
  
  print('Case #{}: {}'.format(j+1,ans), file=file)
