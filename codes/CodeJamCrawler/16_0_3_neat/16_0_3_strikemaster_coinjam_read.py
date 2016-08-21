import sys
from coinjam import coinjam

file_name = sys.argv[1]
file_name_out = "%s.out" % file_name[:len(file_name)-3]
print "printing to %s" % file_name_out

infile = open(file_name, 'r')
line = infile.readlines()[1].strip()
n, j = [int(x) for x in line.split(' ')]
infile.close()

outfile = open(file_name_out, 'w')

ans = coinjam(n, j)
outfile.write('Case #1:\n')
lines = []
for jamcoin in ans:
  coin, lst = jamcoin
  lines.append('%s %s' % (coin, ' '.join([str(x) for x in lst])))
outfile.write('\n'.join(lines))

outfile.close()
