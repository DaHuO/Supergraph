T = int(input())
f = open("pancake.w", "w")

def print_res(i, res):
  f.write("Case #" + str(i+1) + ": " + str(res) + "\n")

for i in range(T):
  pancakes = raw_input()
  res = 0
  see_blank = False
  saw_smiley = False
  for p in pancakes:
    if p == '+':
      if see_blank:
        see_blank = False
        res += 1
        if saw_smiley:
          res += 1
      saw_smiley = True
    else:
      see_blank = True
  if see_blank:
    see_blank = False
    res += 1
    if saw_smiley:
      res += 1    
  print_res(i, res)

f.close()
