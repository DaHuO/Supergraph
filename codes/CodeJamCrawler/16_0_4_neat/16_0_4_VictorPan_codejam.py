# We know original sequence number of tiles K
# We know the complexity C
# S - students == K in small
def solve(k,c,s):
  if s < k:
    return "IMPOSSIBLE"
  if k == 2:
    return "1 "+str(k**c)
  tree = []
  answer = ""
  for i in range(1,k+1):
    tree.append(i)
  for i in range(c-1):
    for j in range(1,len(tree)-1):
      tree[j] = tree[j] + j*tree[len(tree)-1]
    tree[len(tree)-1] = k**(i+2)
  for i in range(len(tree)):
    answer+=str(tree[i])+" "
  return answer

# This is all you need for most Google Code Jam problems.
t = int(input())
for i in range(1, t + 1):
  k, c, s = [int(s) for s in input().split(" ")]
  print("Case #{}: {}".format(i, solve(k,c,s)))
