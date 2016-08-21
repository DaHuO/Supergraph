def solve(S):
  num_flips = 0
  print S
  if len(S) == 1:
    if S[0] == '+':
      return 0
    else:
      return 1
  compare = S[0]
  print 'compare', compare
  for j in range(1, len(S)):
    if S[j] != compare:      
      num_flips += 1
      compare = S[j]
      print 'added', S[j]
  if S[-1] == '-':
    num_flips += 1
  return num_flips  

def print_solution(ans):
  f = open('output_small.txt', 'w')
  for i in range(len(ans)):
    f.write("Case #" + str(i+1) + ": " + str(ans[i]) +"\n")

if __name__ == '__main__':  
  f = open('B-large.in')
  T = int(f.readline())
  answers = [0]*T
  for i in range(T):
    S = f.readline()      
    answers[i] = solve(S.strip())  
    print answers[i]
  print answers
  print_solution(answers)

    