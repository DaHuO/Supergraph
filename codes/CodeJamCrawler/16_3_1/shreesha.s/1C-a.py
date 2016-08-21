t = int(raw_input())
for i in range(t):
  n = int(raw_input())
  inp = map(int, raw_input().split())
  maxi = max(inp)
  ans = ""
  print "Case #%d:" %(i+1),
  while(maxi != 1):
    for j in range(n):
      if inp[j] == maxi:
        ans += chr(65+j)
        inp[j] -= 1
        if len(ans) == 2:
          print ans,
          ans = ""
    if len(ans) == 1:
      print ans,
      ans = ""
    maxi = max(inp)
  for j in range(n-2):
    print chr(65+j),
  print chr(65+n-2)+chr(65+n-1)

