outfile = open('output.txt', 'w')
with open('B-large.in') as f:
    mylist = f.read().splitlines()

for i in range(1, len(mylist)):
    answer = 0
    n = mylist[i]
    print('n =',n)
    print('n[-1:] =',n)
    if(n[-1:] == '-'):
        answer+=1
        print('answer=',answer)
    for j in range(1,len(n)):
        if(n[j-1] != n[j]):
            answer+=1
        print('j=',j,'\tn[j-1]=',n[j-1],'\tn[j]=',n[j],'\tanswer=',answer)

    outfile.write("Case #{}: {}\n".format(i, answer))