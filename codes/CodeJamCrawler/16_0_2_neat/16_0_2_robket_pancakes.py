t = int(raw_input())
for tc in range(1, t+1):
  string = raw_input()
  last_char = string[0]
  switch_count = 0
  for char in string[1:]:
    if last_char != char:
      switch_count += 1
      last_char = char
  if string[-1] == "-":
    switch_count += 1
  print("Case #%d: %d"%(tc, switch_count))
