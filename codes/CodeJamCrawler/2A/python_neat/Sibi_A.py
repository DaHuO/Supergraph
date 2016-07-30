import sys

iFile = open(sys.argv[1],"r")

T = int(iFile.readline().strip())

N_max = 12

R_tree = {}
P_tree = {}
S_tree = {}

start = {"S":"SP", "P":"PR", "R":"SR"}
mid = {"S":"PS", "P":"PR", "R":"SR"}
end = {"S":"PS", "P":"PR", "R":"RS"}

for n in range(1,N_max+1):
  R_string = "R"
  P_string = "P"
  S_string = "S"
  
  for i in range(n):
    tmp_R = ""
    tmp_P = ""
    tmp_S = ""
    for c in range(len(R_string)):
      if i == n-1:
        tmp_R += end[R_string[c]]
        tmp_P += end[P_string[c]]
        tmp_S += end[S_string[c]]
      elif i == n-2:
        tmp_R += mid[R_string[c]]
        tmp_P += mid[P_string[c]]
        tmp_S += mid[S_string[c]]
      else:
        tmp_R += start[R_string[c]]
        tmp_P += start[P_string[c]]
        tmp_S += start[S_string[c]]
        
    R_string = tmp_R
    P_string = tmp_P
    S_string = tmp_S
      
  
  R_tree[n] = R_string
  P_tree[n] = P_string
  S_tree[n] = S_string
  
for t in range(T):
    line = iFile.readline().strip().split()
    
    N = int(line[0])
    R = int(line[1])
    P = int(line[2])
    S = int(line[3])
    
    if R_tree[N].count("R") == R and R_tree[N].count("P") == P and R_tree[N].count("S") == S:
      answer = R_tree[N]
    elif P_tree[N].count("R") == R and P_tree[N].count("P") == P and P_tree[N].count("S") == S:
      answer = P_tree[N]
    elif S_tree[N].count("R") == R and S_tree[N].count("P") == P and S_tree[N].count("S") == S:
      answer = S_tree[N]
    else:
      answer = "IMPOSSIBLE"
    
    output = str(answer)
    
    print("Case #"+str(t+1)+": "+output)
