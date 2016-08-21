from collections import defaultdict
import itertools

cache = defaultdict(float)

def optimize_for_yes_count(probs, N,starting_from, target_yeses, picks_remaining):
  if(starting_from == N):
    if picks_remaining != 0:
      return None, None
    elif target_yeses == 0:
      return (1.0,[])
    else:
      return (0.0,[])
  if picks_remaining == 0:
    if target_yeses == 0:
      return (1.0,[])
    else:
      return (0.0,[])
  
  res = cache.get((starting_from, target_yeses, picks_remaining),None)
  if(res != None):
    return res
  
  best = 0.0
  bl = None
  '''for next_pick in xrange(starting_from, N):
    prob_yes = probs[next_pick]
    prob_no = 1-prob_yes
    if(prob_yes > 0.5):
      yes_res, lst = optimize_for_yes_count(probs, N,next_pick+1, target_yeses - 1, picks_remaining - 1)
      no_res = 1-yes_res
    elif(prob_yes < 0.5):
      no_res, lst = optimize_for_yes_count(probs, N,next_pick+1, target_yeses, picks_remaining - 1)
      yes_res = 1-no_res
    #else:
      
    if yes_res is None or no_res is None:
      prob_success = 0.0
    else:
      prob_success = prob_yes * yes_res + prob_no * no_res
    if (bl is None) or (prob_success > best):
      best = prob_sucess
      bl = [next_pick] + lst
  '''
  cache[(starting_from, target_yeses, picks_remaining)] = (best, bl)
  return best


def do_case(N,K,probs):
  global cache
  cache = defaultdict(float)
  return optimize_for_yes_count(probs, N, 0, K/2, K)
  
def get_tie_prob(K, rp):
  probs = list()
  probs.append(1.0)
  for i in xrange(K-1):
    probs.append(0.0)
  for p in rp:
    probs2 = [0.0] * K
    for i in xrange(K):
      if(i>0):
        probs2[i] = probs[i-1]*p+probs[i]*(1-p)
      else:
        probs2[i] = probs[i]*(1-p)
    probs = probs2
  return probs[K/2]
  
def brute_force(N,K,probs):
  best = 0.0
  #print(probs)
  for combo in itertools.combinations(probs, K):
    #print(combo)
    tie_prob = get_tie_prob(K,combo)
    best = max(best, tie_prob)
  return best
    
f = open("B-small-attempt0.in").read()
lines = f.split("\n")
T = int(lines[0])
out=""
for i in xrange(T):
  parts = lines[i*2+1].split(" ")
  parts2 = lines[i*2+2].split(" ")
  N = int(parts[0])
  K = int(parts[1])
  flts = [float(x) for x in parts2]
  out+="Case #%d: %s\n" % (i+1, brute_force(N,K,flts))
  print(i)
  i+=1
  
open("B-small2.out","w").write(out)
