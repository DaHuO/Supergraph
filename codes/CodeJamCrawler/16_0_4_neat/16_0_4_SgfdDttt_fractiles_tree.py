input_file = "D-small-attempt0.in"
counter = -1
for line in open(input_file, 'r'):
  counter += 1
  if counter == 0:
    continue
  params = line.split()
  K = int(params[0])
  C = int(params[1])
  S = int(params[2])
  tiles_to_clean = set()
  for group in range(1,K/C+1):
    #print("group = " + str(group))
    tile = 1 
    for ind in range((group-1)*C+1, group*C+1):
      #print("tile = " + str(tile))
      tile = (tile-1) * K + ind
    tiles_to_clean.add(tile)
  for additional_tiles in range((K - (K%C))+1, K+1):
    tiles_to_clean.add(additional_tiles)
  answer_str = "Case #" + str(counter) + ": "
  if len(tiles_to_clean) > S:
    answer_str += "IMPOSSIBLE"
  else:
    for tile in tiles_to_clean:
      answer_str += str(tile) + " "
  answer_str = answer_str.strip()
  print answer_str
