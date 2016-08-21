IN_FILE = "A-large.in"

infile = open(IN_FILE)
out = open("A_out.txt","w")

cases = int(infile.readline())

for case in range(cases):
    print "Case #%i" %(case+1)
    out.write("Case #%i: " %(case+1))
    n = int(infile.readline())
    if n == 0:
        out.write("INSOMNIA\n")
        continue
        
    ans = 0
    seen = [0]*10
    num = 0
    while 0 in seen:
        num += n
        #print num
        #print seen
        for digit in str(num):
            seen[int(digit)] = 1
            
    out.write("%i\n" %(num))
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()