def sort_tournament(tournament):
  if len(tournament) == 1:
    return tournament
  else:
    l = len(tournament)/2
    t1 = sort_tournament(tournament[:l])
    t2 = sort_tournament(tournament[l:])
    if t1 < t2:
      return t1 + t2
    else:
      return t2 + t1

def correct_tournament(N, R, P, S):
  for seed in [0,1,2]:
    tournament = generate_tournament(N, seed)
    p = tournament.count(0)
    r = tournament.count(1)
    s = tournament.count(2)
    if p==P and r==R and s==S:
      return tournament

def generate_tournament(N, seed):
  tournament = [seed]
  for _ in range(N):
    tournament = sum(([x, (x+1)%3] for x in tournament), [])
  return tournament

T = int(raw_input())
for test_case in range(T):
  [N, R, P, S] = [int(x) for x in raw_input().split()]
  if max(R,P,S) > min(R,P,S) + 1:
    answer = "IMPOSSIBLE"
  else:
    answer = correct_tournament(N, R, P, S)
    answer = sort_tournament(answer)
    alphabet = "PRS"
    answer = "".join(alphabet[x] for x in answer)
  print "Case #%s: %s"%(test_case+1, answer)
