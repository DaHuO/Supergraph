def tts(n):
  if n == 0: return 'INSOMNIA'
  seen = [False for i in range(0, 10)]
  x = n
  while not all_seen(seen):
    mark_digits(seen, x)
    if all_seen(seen):
      return x
    x += n

def mark_digits(array, x):
  while x > 9:
    last_digit = x % 10
    array[last_digit] = True
    x = x // 10
  array[x] = True

def all_seen(array):
  for i in array:
    if not i: return False
  return True


if __name__ == '__main__':
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
  # This is all you need for most Google Code Jam problems.
  t = int(input())  # read a line with a single integer
  for i in range(1, t + 1):
    #n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    n = int(input())
    print('Case #%d: %s' % (i, str(tts(n))))
