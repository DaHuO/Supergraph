def get_ans(s):
  ls = []
  cs = ['']
  for i in s :
    added = set()
    for each in cs:
      added.add(each + i)
      added.add(i + each)
    added = list(added)
    ls = ls + added
    cs = added
  return sorted(ls)[-1]


fp = open('a.in' , 'r')
fout = open('a.out' , 'w+')

for i in range(int(fp.readline())):
  s = fp.readline().replace('\n' , '')
  ans = get_ans(s)
  fout.writelines("Case #" + str(i+1) + ": " + ans + '\n')

fp.close()
fout.close()

  
