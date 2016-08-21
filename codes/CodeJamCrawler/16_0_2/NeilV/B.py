IN_FILE = "B-large.in"

infile = open(IN_FILE)
out = open("B_out.txt","w")

cases = int(infile.readline())

for case in range(cases):
    print "Case #%i" %(case+1)
    out.write("Case #%i: " %(case+1))
    
    stack = infile.readline().strip()
    print stack
    stack = stack.rstrip("+")
    if stack == "":
        out.write("0\n")
        print 0
    else:    
        ans = 1
        for i in range(1,len(stack)):
            if stack[i] != stack[i-1]:
                ans += 1
        out.write("%i\n" %ans)
        print ans
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()