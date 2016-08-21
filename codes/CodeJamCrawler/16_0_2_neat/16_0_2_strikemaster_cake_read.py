import sys
from cake import cake

file_name = sys.argv[1]
file_name_out = "%s_out" % file_name
print "printing to %s" % file_name_out

infile = open(file_name, 'r')
inputs = []
for cakes in infile.readlines():
  inputs.append(list(cakes.strip()))
infile.close()

inputs = inputs[1:]
answers = []
for idx,inp in enumerate(inputs):
  ans = cake(inp)
  answers.append('Case #%s: %s' % (idx+1, ans))


outfile = open(file_name_out, 'w')
outfile.write('\n'.join(answers))
outfile.close()