
def mult(n):
  i = 1
  while True:
    yield n*i
    i += 1

def sheep(n):
  nums = set()
  itern = 0
  for multiple in mult(n):
    if itern == 1000000:
      return 'INSOMNIA'
    for char in str(multiple):
      nums |= {char}
    if len(nums) == 10:
      return multiple
    itern += 1
