import sys

firstline = True
n = 1
for line in sys.stdin:
    if firstline:
        firstline = False
    else:
        line = line.strip()

        def removeDupsSorted(List):
            res_ind = 1
            ip_ind = 1
            while ip_ind != len(List):
                if List[ip_ind] != List[ip_ind - 1]:
                    List[res_ind] = List[ip_ind]
                    res_ind += 1
                ip_ind += 1
            string = ''.join(List[0:res_ind])
            return string

        lst = removeDupsSorted(list(line))
        cnt = 2 * lst.count('-') - 1

        if line.startswith('+'):
            cnt += 1

        print 'Case #' + str(n) + ': ' + str(cnt)
        n += 1


# add one if starts with a plus
# strip last +
# 2n-1 minuses



  #       line = line.strip()

  #       val_queue = []
  #       seen = set()

  #       def generate(x):
  #           vals = list(x)
  #           for i in range(len(vals) + 1):
  #               rev = list(reversed(x[:i]))
  #               def flipped(p):
  #                   if p == '+':
  #                       return '-'
  #                   else:
  #                       return '+'
  #               rev = [flipped(j) for j in rev]
  #               out = rev + list(x[i:])
  #               yield ''.join(out)

  #       target = ''.join(['+' for i in range(len(line))])

  #       val_queue.append((line, 0))
  #       seen.add(line)

  #       for obj in val_queue:
  #           if obj[0] == target:
  #               print 'Case #' + str(n) + ': ' + str(obj[1])
  #               q = (obj[0], obj[1])
  #               break

  #           q = None
  #           for x in generate(obj[0]):
  #               if x == target:
  #                   print 'Case #' + str(n) + ': ' + str(obj[1] + 1)
  #                   q = (x, obj[1] + 1)
  #                   break
  #               if x not in seen:
  #                   val_queue.append((x, obj[1] + 1))
  #                   seen.add(x)
  #           if q:
  #               break

  #       n += 1


# add one if starts with a plus
# strip last +
# 2n-1 minuses

