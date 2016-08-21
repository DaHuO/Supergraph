import sys

def evac(filename):
  parties = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  with open(filename, 'r') as f:
    T = int(f.readline().rstrip())
    for t in xrange(T):
      N = int(f.readline().rstrip())
      num_sen = f.readline().rstrip().split(" ")
      sen_dict = {parties[i]: int(num_sen[i]) for i in xrange(len(num_sen))}
      # print sen_dict
      total = sum(sen_dict.values())
      e = ''
      while sen_dict:
        for r in xrange(2):
          sortsen = sorted(sen_dict.items(), key=lambda (x): x[1])
          if sortsen:
            # if r == 0:
              # print sortsen
            if sen_dict.values() == [1]*len(sortsen) and len(sortsen) % 2 != 0 and sen_dict[sortsen[-1][0]] > 0:
              e += sortsen[-1][0]
              sen_dict[sortsen[-1][0]] -= 1
              break
            p = sortsen[-1][0]
            if sen_dict[p] > 0:
              sen_dict[p] -= 1
              e += p
            else:
              del sen_dict[p]
        e += ' '
      print "Case #{}: {}".format(t+1, e)

if __name__ == '__main__':
  evac(sys.argv[1])