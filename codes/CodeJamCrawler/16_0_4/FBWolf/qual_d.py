import os

fin = open('D-small-attempt0.in', 'r')
fout = open('D.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  parts = line.strip().split()
  K, C, S = [int(x) for x in parts]

  out_str = 'Case #%d: ' % (i)
  if S < K:
    out_str += 'IMPOSSIBLE'
  else:
    # res = solve_n(n)

    out_str += ' '.join([str(x+1) for x in range(S)])
  print out_str
  fout.write(out_str + '\n')
fin.close()
fout.close()
