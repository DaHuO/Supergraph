def solve(inp):
  if (inp == 0):
    return "INSOMNIA"
  i = 1
  mem = [0 for j in range(10)]
  while(0 in mem):
    for digit in digits(i*inp):
      mem[digit] = 1
    i += 1
  return (i-1)*inp

def digits(inp):
  if inp < 0:
    inp *= -1
  digits = []
  if inp == 0:
    return [0]
  while inp:
    digits.append(inp % 10)
    inp //= 10
  return digits


f = open('in.txt', 'r')

o = open('out.txt', 'w')

k = 1
for line in list(f)[1:]:
  o.write("Case #"+str(k)+": ")
  sol = solve(int(line.rstrip()))
  o.write(str(sol)+"\n")
  k += 1

f.close()
o.close()
