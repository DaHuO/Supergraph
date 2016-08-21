import sys

def min_flips( S ):
  i=0
  n=len(S)
  while '-' in S:
    i += 1
    m = n
    if S[0] == '-':
      if '+' in S:
        m = S.index('+')
    else:
        m = S.index('-')
    # flip stack 0:m
    T = S[0:m]
    for j in range(0,m):
      S[j] = '+' if T[m-1-j] == '-' else '-'
#    print S
  return i

# get input filename from first arg
in_path = sys.argv[1]
# read input text file to list of strings, 1 per line
with open(in_path, 'r') as in_file:
  in_list = in_file.read().splitlines()

# convert strings to ints (and skip first string)
in_list = [s for s in in_list[1:] ]

#print in_list

out_list = [ min_flips(list(s)) for s in in_list ]

for i, x in enumerate(out_list):
  print 'Case #{}: {}'.format(i+1, x)
