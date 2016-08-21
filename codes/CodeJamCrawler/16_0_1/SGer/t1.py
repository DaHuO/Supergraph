def count_sheep(n):
  if n == 0:
    return "INSOMNIA"
  else:
    digits = []
    i = 1
    k = n
    while len(digits) < 10:
      for ch in str(k):
        if ch not in digits:
          digits.append(ch)
      i += 1
      k = n * i
    return k-n

infile = open("A-large.in",'r')
outfile = open("a1.out",'w')
T = int(infile.readline())
nums = infile.readlines()
i = 1
for num in nums:
  outfile.write("Case #" + str(i) + ": " + str(count_sheep(int(num))) + '\n')
  i += 1
infile.close()
outfile.close()
