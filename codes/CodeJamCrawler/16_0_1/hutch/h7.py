noOfCases = int(raw_input())

res = []

flag = False
output = open("output_sheep_count.txt","w+")
for i in xrange(1,noOfCases+1):
    li = set()
    number =int(raw_input())
    for j in xrange(1,100):
      n = str(j*number)
      li = li.union(set(n))
      if(len(li)==10):
          flag = True
          output.write("Case #" + str(i) + ": " + n + "\n")
          break
    if flag == False:
        output.write("Case #" + str(i) + ": " + "INSOMNIA" + "\n")
    flag = False