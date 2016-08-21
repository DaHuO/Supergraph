t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  K, C, S = [int(s) for s in input().split(" ")]  # read a list of integers, 3 in this case
  print("Case #{}: {} ".format(i, " ".join([str(e) for e in range(1,K+1)])))


