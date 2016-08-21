T = int(input())
for t in range(1, T+1):
  S = input().strip()
  S = S + '+'
  ans = 0
  for i in range(len(S)-1):
    if S[i] != S[i+1]:
      ans += 1
  # print('{}'.format(ans))
  print('Case #{}: {}'.format(t, ans))
