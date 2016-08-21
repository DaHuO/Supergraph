f = open('A-large.in', 'r+')
input_count = int(f.readline())
p = open('large.out', 'w')
res = "INSOMNIA"
def markSeen(lst, seen):
  seen.update(set(lst))
  return seen
  #print "seen: ", list(seen)
def allSeen(seen):
  return seen.issuperset(set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']))
def test(start_number):
  seen = set([])
  if int(start_number) <= 0:
    return "INSOMNIA"
  last_num = start_number
  mult = 1
  while (not allSeen(seen)):
    last_num = str(int(start_number) * mult)
    seen = markSeen(list(last_num), seen)
    mult += 1
  return last_num
count = 1
while count <= input_count:
  start_number = f.readline()
  p.write("Case #" + str(count) + ": " + str(test(start_number))+"\n")
  count += 1