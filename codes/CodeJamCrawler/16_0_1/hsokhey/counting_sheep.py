# counting_sheep.py
t = raw_input()

for i in xrange(int(t)):
    n = raw_input()
    num_str = {}
    final_num = -1
    count = 1
    flag = False
    n1 = int(n) 
    while (not flag):
        
        num_str = set(num_str).union(set(list(str(n1))))
        #print num_str
        if len(num_str) == 10:
            flag = True
            final_num = n1
            break
        n2 = n1
        count = count + 1
        n1 = count * int(n)
        #print count, n1
        if (n2 == n1):
            print "Case #"+str(i+1)+": INSOMNIA"
            final_num = -2 
            break
        else:
            continue

    if final_num != -1 and final_num != -2:
        print "Case #"+str(i+1)+": "+str(final_num)

        
            
        
        
