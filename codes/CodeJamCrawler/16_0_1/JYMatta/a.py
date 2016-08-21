
def last_number(x):
  numbers = {}
  for i in range(1,100):    # limit to 100 trials
    y = x * i
    nums = get_numbers(y)
    for num in nums:
      numbers[num] = True
    if len(numbers) >= 10:
      return y
  return "INSOMNIA"


def get_numbers(y):
  y = str(y)
  out = []
  for i in range(10):
    if str(i) in y:
      out.append(i)
  return out

f = open('input.txt')
out = open('output.txt', 'w')
size = 0
casenum =0
for line in f:
  if size ==0:
    size = int(line)
  else:
    l = last_number(int(line))
    c = "Case #" + str(casenum) + ': ' + str(l)
    print c
    out.write(c+"\n")
  casenum += 1