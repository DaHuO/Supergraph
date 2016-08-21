import sys
from sheep import sheep

file_name = sys.argv[1]
file_name_out = "%s_out" % file_name
print "printing to %s" % file_name_out

infile = open(file_name, 'r')
inputs = []
for num in infile.readlines():
  inputs.append(int(num.strip()))
infile.close()

inputs = inputs[1:]
answers = []
for idx,inp in enumerate(inputs):
  ans = sheep(inp)
  answers.append('Case #%s: %s' % (idx+1, ans))


outfile = open(file_name_out, 'w')
outfile.write('\n'.join(answers))
outfile.close()