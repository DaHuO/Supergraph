import string



def evacuate_senate(num, parties):
  ##  if num == 2:
  #      if parties[0] == parties[1]:
  #          return " ".join(["AB" for i in range(len(parties[0]))])
  #      if parties[0] > parties[1]:
  #          return "A " + " ".join(["AB" for i in range(len(parties[1]))])
  #      else:
  #          return "B " + " ".join(["AB" for i in range(len(parties[0]))])
    p = string.letters[:26]
    plan = []
    while sum(parties) != 0:
        if sum([1 for i in parties if i != 0]) > 2:
            m = parties.index(max(parties))
            l = p[m]
            plan.append(l)
            parties[m] -= 1
        else:
            vals = [i for i in range(len(parties)) if parties[i] != 0]
            l1 = p[vals[0]]
            l2 = p[vals[1]]
            if parties[vals[0]] == parties[vals[1]]:
                plan = plan + [l1+l2 for i in range(parties[vals[0]])]
            elif parties[vals[0]] > parties[vals[1]]:
                plan = plan +  [l1]+[l1+l2  for i in range(parties[vals[1]])]
            else:
                plan = plan +  [l2]+[l1+l2 for i in range(partiesvals[[0]])]
            break
    return string.upper(" ".join(plan))
            
    
    


n = int(raw_input())
for i in range(n):
    num = eval(raw_input())
    parties = map(int, raw_input().split() )
    plan = evacuate_senate(num, parties)
    print "Case #{0}: {1}".format(i+1, plan)
