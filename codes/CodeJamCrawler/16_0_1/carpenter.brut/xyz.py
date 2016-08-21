j=2 #counter for N
i=0 #counter for list
c=1 #counter for cases
list1=['1','2','3','4','5','6','7','8','9','0']
temp_list=list1[:]
t = int(raw_input())
for c in xrange(1, t + 1):
    n=raw_input()
    temp_n=n
    if int(n)==0:
        print 'Case #{}: INSOMNIA'.format(c)
    else:
        while temp_list:
            for digit in temp_n:
                while i<len(temp_list):
                    if digit==temp_list[i]:
                        temp_list.pop(i)
                    else:
                        i+=1
                i=0
            temp_n=str(int(n)*j)
            j+=1
        temp_n=int(n)*(j-2)
        j=2
        temp_list=list1[:]
        print "Case #{}: {}".format(c, temp_n)
