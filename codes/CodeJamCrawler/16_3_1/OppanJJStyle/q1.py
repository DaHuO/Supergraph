# imports

from Queue import PriorityQueue

# code

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def make_parties(l):
  return [[-l[i], ALPHABETS[i]] for i in xrange(len(l))]

def evacuation_plan(parties):
  pq = PriorityQueue()
  for p in parties:
    pq.put(p)
  while not pq.empty():
    a = pq.get()
    first = a[1]
    a[0] += 1
    b = pq.get()
    second = b[1]
    b[0] += 1
    if pq.qsize() == 1 and a[0] == 0 and b[0] == 0:
      b[0] -= 1
      pq.put(b)
      yield str(first)
    else:
      if a[0] != 0:
        pq.put(a)
      if b[0] != 0:
        pq.put(b)
      yield str(first) + str(second)

if __name__ == "__main__":
  g = open("output", "w")
  with open("A-large.in") as f:
    num_cases = 0
    read_num_cases = False
    c = 1
    num_parties = None
    for line in f:
      if not read_num_cases:
        read_num_cases = True
        num_cases = int(line)
      else:
        if num_parties is None:
          num_parties = int(line)
        else:
          parties = make_parties([int(n) for n in line.split()])
          evac = evacuation_plan(parties)
          g.write("Case #" + str(c) + ":")
          for e in evac:
            g.write(" " + e);
          g.write("\n")
          num_parties = None
          c += 1
        
    g.close()
