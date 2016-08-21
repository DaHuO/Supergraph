# Counting Sheep
import sys
f = open(sys.argv[1], 'r')

t = int(f.readline())

for ind, n in enumerate([int(x) for x in f]):
  nums_remaining = set(range(10))
  
  current_num = n
  print("Case #{}: ".format(ind + 1), end="")
  for _ in range(1000000):
    for digit in str(current_num):
      try:
        nums_remaining.remove(int(digit))
      except:
        continue
    if len(nums_remaining) == 0:
      print(current_num)
      break
    current_num += n
  else:
    print("INSOMNIA")
