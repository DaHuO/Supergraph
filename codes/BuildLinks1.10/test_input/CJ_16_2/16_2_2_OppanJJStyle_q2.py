# imports



# code

def where_zero(l):
  return [i for i in xrange(len(l)) if l[i] is None]

def to_list(s):
  return [int(c) if c.isdigit() else None for c in s]

def to_int(l):
  res = 0
  for c in l:
    res *= 10
    res += c
  return res

def increment(d, keys):
  for i in xrange(len(keys) - 1, -1, -1):
    if d[keys[i]] < 9:
      d[keys[i]] += 1
      if i < len(keys) - 1:
        for j in xrange(i + 1, len(keys)):
          d[keys[j]] = 0
      return True
  return False

def zeroize(d, keys):
  for k in keys:
    d[k] = 0

def apply_dict(l, d, keys):
  for k in keys:
    l[k] = d[k]

def analyze(x, y):
  list_x = to_list(x)
  list_y = to_list(y)
  l = min_difs(list_x, where_zero(list_x), list_y, where_zero(list_y), float('inf'))
  if len(l) == 1:
    return l[0][0], l[0][1]
  else:
    lx = min_x(l)
    if len(lx) == 1:
      return lx[0][0], lx[0][1]
    else:
      ly = min_y(lx)
      if len(ly) == 1:
        return ly[0][0], ly[0][1]
      else:
        return None

def min_difs(list_x, where_zero_x, list_y, where_zero_y, min_dif):
  results = []
  d_x = {i: 0 for i in where_zero_x}
  keys_x = d_x.keys()
  keys_x.sort()
  d_y = {i: 0 for i in where_zero_y}
  keys_y = d_y.keys()
  keys_y.sort()
  valid = True
  while valid:
    apply_dict(list_x, d_x, keys_x)
    apply_dict(list_y, d_y, keys_y)
    int_x = to_int(list_x)
    int_y = to_int(list_y)
    dif = abs(int_x - int_y)
    if dif < min_dif:
      results = []
      min_dif = dif
    if dif == min_dif:
      results.append((int_x, int_y))

    if not increment(d_x, keys_x):
      if not increment(d_y, keys_y):
        valid = False
      else:
        zeroize(d_x, keys_x)
  return results

def min_x(l):
  minx = float('inf')
  results = []
  for x,y in l:
    if x < minx:
      results = []
      minx = x
    if x == minx:
      results.append((x,y))
  return results

def min_y(l):
  miny = float('inf')
  results = []
  for x,y in l:
    if y < miny:
      results = []
      miny = y
    if y == miny:
      results.append((x,y))
  return results

if __name__ == "__main__":
  g = open("output", "w")
  with open("B-small-attempt0.in") as f:
    num_cases = 0
    read_num_cases = False
    c = 1
    for line in f:
      if not read_num_cases:
        read_num_cases = True
        num_cases = int(line)
      else:

        if line[-1] == '\n':
          line = line[:-1]
        inputs = line.split(" ")
        x, y = analyze(inputs[0], inputs[1])
        g.write("Case #" + str(c) + ": " + str(x).zfill(len(inputs[0])) + " " + str(y).zfill(len(inputs[1])) + "\n")

        c += 1
    g.close()