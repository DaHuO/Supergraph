import sys

def evac_plan( S ):
  # convert list of Pi to dict
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
              'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  alphabet.sort()
  P = dict()
  for i, N in enumerate(S):
    P[alphabet[i]] = int(N)

#  print sum(P.values())
  # build evac plan as string of 1- or 2-char steps, space-separated
  plan = ""
  while sum(P.values()) != 0:
    step = ""
    # find party with largest N
    v = list(P.values())
    k = list(P.keys())
    p = k[v.index(max(v))]
#  print p
    # decrement p, add to plan
    P[p] = P[p] - 1
    step += str(p)
    
    # cannot leave just 1 party remaining at end of step
    if sum(P.values()) == 2:
      plan += step + " "
      continue

    # find party with largest N
    v = list(P.values())
#    k = list(P.keys())
    p = k[v.index(max(v))]
    # decrement p, add to plan
    P[p] = P[p] - 1
    step += str(p)
    plan += step + " "
  return plan

# get input filename from first arg
in_path = sys.argv[1]
# read input text file to list of strings, 1 per line; skip [0]: 'T'
with open(in_path, 'r') as in_file:
  in_list = in_file.read().splitlines()

# convert strings to ints (and skip first string)
in_list = [s.split(' ') for s in in_list[2::2] ]

#print in_list

out_list = [ evac_plan(s) for s in in_list ]

for i, x in enumerate(out_list):
  print 'Case #{}: {}'.format(i+1, x)
