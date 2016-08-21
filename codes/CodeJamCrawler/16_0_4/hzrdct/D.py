T = int(input())
for t in range(1, T+1):
  K, C, S = map(int, input().split())
  indices_to_check = [str(i) for i in range(1, K**(C)+1, K**(C-1))] 
  indices_to_check = ' '.join(indices_to_check)
  print("Case #{}: {}".format(t, indices_to_check))
