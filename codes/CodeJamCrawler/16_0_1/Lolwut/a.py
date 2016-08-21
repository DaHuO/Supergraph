input = open("A-large.in")
started = False
i = 0
for l in input:
  if i == 0:
    i = 1
    continue
  num = int(l)
  if num == 0:
    print "Case #" + str(i) + ": INSOMNIA"
  else:
    j = 1
    nums = [False]*10
    temp = num
    while True:
      for k in str(temp):
        nums[int(k)] = True
      if not False in nums:
        print "Case #" + str(i) + ": " + str(temp)
        break
      j += 1
      temp = num * j
  i += 1
  
