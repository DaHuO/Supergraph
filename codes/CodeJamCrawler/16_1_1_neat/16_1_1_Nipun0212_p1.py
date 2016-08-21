n = input()
for i in range(n):
    z = raw_input()
    x = len(z)
    y =""
    for j in range(x):
        #print j
        if(j==0):
            y = z[j]
        else:
            if(y[0]>z[j]):
                y = y + z[j]
            else:
                y = z[j] + y
    print "CASE #" + str(i+1) + ":" + " " + y
        
