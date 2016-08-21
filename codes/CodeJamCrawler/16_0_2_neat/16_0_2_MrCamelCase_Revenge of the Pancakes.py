inp = open("B-large.in.txt").readlines()
out = open("Q2OUT.txt",'w')
limit = int(inp[0].rstrip())
qn = 0
for i in inp[1:]:
    qn+=1
    complexity = 0
    array = list(reversed([letter for letter in i.rstrip()]))
    last = "+"
    for item in array:
        if item!=last:
            last = item
            complexity+=1
    #print(complexity)
    out.write("Case #%s: %s"%(str(qn),str(complexity)))
    if qn != limit:
        out.write("\n")
out.close()
