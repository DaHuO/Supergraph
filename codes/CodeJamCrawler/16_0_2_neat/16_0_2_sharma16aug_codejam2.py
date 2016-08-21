test=input() 
p=set("+")
m=set("-")
val=1
while test is not 0:
    count=0
    list_string=list(raw_input())
    list_set=set(list_string)
    if list_set.issubset(p):
        print "Case #"+str(val)+":","0"
        val+=1
    elif list_set.issubset(m):
        print "Case #"+str(val)+":","1"
        val+=1
    else:
        while len(list_set) is not 1:
            j=0
            i=0
            if list_string[i]=="+":
                ind=list_string.index("-")
                j=ind
            else:
                ind=list_string.index("+")
                j=ind
            for i in xrange(0,ind):
                if list_string[i]=="+":
                    list_string[i]="-"
                else:
                    list_string[i]="+"
            count+=1
            list_set=set(list_string)
        if list_set.issubset(p):
            print "Case #"+str(val)+":",count
            val+=1
        else:
            print "Case #"+str(val)+":",count+1
            val+=1       
    test-=1
    
