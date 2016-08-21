import sys

def count_sheep( N ):
  if (N==0):
    return "INSOMNIA"
  M=0
  digits = set()
  while len(digits) < 10:
    M+=N
    for digit in str(M):
      digits.add(digit)
#    print digits
  return str(M)

# get input filename from first arg
in_path = sys.argv[1]
# read input text file to list of strings, 1 per line
with open(in_path, 'r') as in_file:
  in_list = in_file.read().splitlines()

# convert strings to ints (and skip first string)
in_list = [int(i) for i in in_list[1:] ]

#print in_list

out_list = [ count_sheep(n) for n in in_list ]

for i, x in enumerate(out_list):
  print 'Case #{}: {}'.format(i+1, x)
