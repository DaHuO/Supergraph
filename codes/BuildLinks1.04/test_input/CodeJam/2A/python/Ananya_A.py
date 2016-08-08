import fileinput

winner = [[-1,0,2],[0,-1,1],[2,1,-1]]
other_index_arr = [[-1,2,1],[2,-1,0],[1,0,-1]]
int_to_char = ['P', 'R', 'S']
win_map = {}
win_map['P'] = 'PR'
win_map['S'] = 'PS'
win_map['R'] = 'RS'

def get_init_string(last, N):
  if N == 0:
    return last
  else:
    new_one = win_map[last]
    s1 = get_init_string(new_one[0], N-1)
    s2 = get_init_string(new_one[1], N-1)
    if s1 < s2:
      return s1 + s2
    else:
      return s2 + s1

def solve(N, counts):
  # Get the winner (deterministic)
  while(sum(counts) > 1):
    min_index = counts.index(min(counts))
    max_index = counts.index(max(counts))
    assert(min_index != max_index)

    new_counts = [0,0,0]
    other_index = other_index_arr[min_index][max_index]
    assert(other_index != -1 and other_index != min_index and other_index != max_index)
    amount = counts[max_index] - counts[other_index]
    if amount > counts[min_index]:
      return "IMPOSSIBLE"

    counts[min_index] -= amount
    counts[max_index] -= amount
    new_counts[winner[max_index][min_index]] += amount
    if counts[min_index] % 2 == 1:
      return "IMPOSSIBLE"

    amount = counts[min_index] / 2
    new_counts[winner[min_index][max_index]] += amount
    new_counts[winner[min_index][other_index]] += amount
    counts[max_index] -= amount
    counts[other_index] -= amount

    assert(counts[max_index] == counts[other_index])
    new_counts[winner[max_index][other_index]] = counts[max_index]
    counts = new_counts
  
  last = counts.index(max(counts));
  assert(counts[last] == 1)
  answer = get_init_string(int_to_char[last], N)
  return answer

num_cases = int(raw_input())
for case in range(1,num_cases+1):
  inputs = raw_input().split()
  N = int(inputs[0])
  R = int(inputs[1])
  P = int(inputs[2])
  S = int(inputs[3])
  answer = solve(N, [P, R, S])
  print("Case #%d: %s" % (case, answer))
