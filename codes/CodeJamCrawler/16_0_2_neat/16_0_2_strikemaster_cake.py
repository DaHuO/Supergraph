HAPPY = '+'
SAD = '-'

def flip(cakes):
  flipped = []
  for cake in reversed(cakes):
    flipped.append(SAD if cake == HAPPY else HAPPY)
  return flipped

# Format is list of + and -. First element is top.
# Just try to get deepest one flipped.
def cake(cakes):
  num_flips = 0
  current_state = cakes
  # Find first - from the back.
  while SAD in current_state:
    last_ind = list(reversed(current_state)).index(SAD)
    sub_prob = current_state[:len(current_state) - last_ind]
    if len(sub_prob) == 1 or sub_prob[0] == SAD:
      num_flips += 1
      current_state = flip(sub_prob)
    else:
      num_flips += 2
      # Flip first number of happies
      num_first = sub_prob.index(SAD)
      sub_prob = [SAD] * num_first + sub_prob[num_first:]
      current_state = flip(sub_prob)
  return num_flips

