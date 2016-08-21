def proc(key, letters, idx, result, char_occr):
  if key in letters:
    amt = char_occr.get(key)
    if amt is not None and amt is not 0:
      result[idx] = amt
      for ch in letters:
        char_occr[ch] -= amt

  return result, char_occr

t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  input = raw_input()
  char_occr = dict()
  for ch in input:
    if char_occr.get(ch) is None:
      char_occr[ch] = 0

    char_occr[ch] += 1

  result = [0]*10
  result, char_occr = proc('Z', 'ZERO', 0, result, char_occr)
  result, char_occr = proc('X', 'SIX', 6, result, char_occr)
  result, char_occr = proc('W', 'TWO', 2, result, char_occr)
  result, char_occr = proc('S', 'SEVEN', 7, result, char_occr)
  result, char_occr = proc('V', 'FIVE', 5, result, char_occr)
  result, char_occr = proc('G', 'EIGHT', 8, result, char_occr)
  result, char_occr = proc('T', 'THREE', 3, result, char_occr)
  result, char_occr = proc('R', 'FOUR', 4, result, char_occr)
  result, char_occr = proc('O', 'ONE', 1, result, char_occr)
  result, char_occr = proc('E', 'NINE', 9, result, char_occr)
  
  res_str = ""
  for idx in range(0,10):
    res_str += (str(idx)*result[idx])

  print "Case #{}: {}".format(i, res_str)
  

