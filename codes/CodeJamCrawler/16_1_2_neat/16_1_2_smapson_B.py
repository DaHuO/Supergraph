def subtract(a,b):
  if len(a) > len(b):
    return subtract(b,a)
  a,b = sorted(a), sorted(b)
  subtracted = []
  while a:
    A, B = a.pop(), b.pop()
    while b and A != B:
      subtracted.append(B)
      B = b.pop()
  return sorted(subtracted + b) 
      
T = int(raw_input())
for test_case in range(T):
  N = int(raw_input())
  rows = [[int(x) for x in raw_input().split()] for _ in range(2*N-1)]
  flagged = []
  missing_numbers = []
  #first row
  for i in range(N):
    min_number = min(rows[row_n][i] for row_n in range(2*N-1) if row_n not in flagged)
    min_rows = [row_n for row_n in range(len(rows)) if rows[row_n][i] == min_number and row_n not in flagged]
    flagged += min_rows
    required_h_lol = [rows[row_n] for row_n in min_rows]
    required_h = [item for sublist in required_h_lol for item in sublist]
    required_v = [x[i] for x in rows]
    if len(required_h) == N:
      sub = subtract(required_v, required_h)
      answer = sorted([min_number] + sub)
      answer_string = " ".join([str(s) for s in answer])
      print "Case #%s: %s"%(test_case+1, answer_string)
      break
