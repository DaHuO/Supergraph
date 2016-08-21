ipname = input("Enter the name of input file : ")
ip = open(ipname, "r")
o1 = "Output "
extension = ".txt"
outputname = o1 + ipname[:-4] + extension
out = open(outputname, "w")
    
# Scanning all the Test cases
t = ip.readline()
t = int(t)

# Starting the loop T times
#for i in range(T):
    
    # #######.. Main program code here ..####### #
#t = input();t = int(t)

for t_i in range(t):
    n = ip.readline(); n = int(n)
    s = n
    digit = [0]*10
    if(n==0):
        #print("Case #"+str(t_i+1)+": INSOMNIA")
	    out.writelines("Case #%d: INSOMNIA\n" % (t_i+1))
    else:
        i=0;l=n
        while(sum(digit)!=10):
            n = s*(i+1)
            i = i+1
            l=n
            while(l!=0):
                k = l%10
                digit[k] = 1
                l = l//10
        #print("Case #"+str(t_i+1)+": "+str(n))
        out.writelines("Case #%d: %d\n" % (t_i+1, n))
        #out.writelines("Case #%d: \n" % (i+1, ))

ip.close()
out.close()