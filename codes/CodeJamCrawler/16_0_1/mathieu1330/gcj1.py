# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())# [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  current_n = n
  value = n

  if n == 0:
      print("Case #{}: INSOMNIA".format(i))
      continue

  digits = [False for j in range(10)]

  while not all(x for x in digits):
      counter = 0
      while value != 0:
          digits[int(value%10)] = True
          value //= 10
          counter += 1
      current_n += n
      value = current_n

  print("Case #{}: {}".format(i, current_n-n))
