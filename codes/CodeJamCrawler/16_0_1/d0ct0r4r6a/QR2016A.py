T= int (raw_input())
counter=1

while(counter<=T):
    Z=[]
    k=1
    N= int (raw_input())
    if N==0:
        print "Case #{}: INSOMNIA".format(counter)
    else:
        while (len(Z)!=10):
            Y= [int(i) for i in str(N*k)]
            for y in Y:
                if y not in Z:
                    Z.append(y)
            k=k+1
        print "Case #{}: {}".format(counter,(k-1)*N)
    counter=counter+1
