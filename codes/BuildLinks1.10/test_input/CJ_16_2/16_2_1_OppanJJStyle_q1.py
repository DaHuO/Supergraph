# imports



# code

candidates = ["ZERO", "EIGHT", "SEVEN", "SIX", "FIVE", "TWO", "FOUR", "NINE", "THREE", "ONE"]

d = { "ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}

def exists(line, possibilities, i):
  matched = set()
  c = candidates[i]
  for char in c:
    for j in possibilities:
      if not j in matched and line[j] == char:
        matched.add(j)
        break
    else:
      return False
  return matched

def decode_helper(line, possibilities, i, result):
  if i >= len(candidates):
    return None
  if not possibilities:
    return result
  matched = exists(line, possibilities, i)
  if matched:
    new_possibilities = possibilities.copy()
    new_result = result + [d[candidates[i]]]
    return decode_helper(line, new_possibilities, 0, new_result)
  else:
    return decode_helper(line, possibilities, i + 1, result)

def decode(line):
  for i in xrange(len(candidates)):
    result = decode_helper(line, set(range(len(line))), i, [])
    if result is not None:
      result.sort()
      return "".join([str(r) for r in result])

if __name__ == "__main__":
  g = open("output", "w")
  with open("A-small-attempt1.in") as f:
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
        g.write("Case #" + str(c) + ": " + str(decode(line)) + "\n")

        c += 1
    g.close()