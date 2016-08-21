__author__ = 'SATYANARAYANAREDDY'
iter_list = []
for e in range(int(input())):
    iter_list.append(int(input()))

for k in range(len(iter_list)):
    N = iter_list[k]
    if N==0:
        print "Case #"+str(k+1)+": "+"INSOMNIA"
    else:
        i=0
        li = [0]*10
        NotDone = True
        while(NotDone):
            curr_N = N*(i+1)
            i+=1

            for each in str(curr_N):
                li[int(each)] = 1

            NotDone = li != [1]*10
        print "Case #"+str(k+1)+": "+str(curr_N)