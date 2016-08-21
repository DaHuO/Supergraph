prob1 = open('A-large.in', 'r')


T = int(prob1.readline())
answers=[]
for i in xrange(T):

    n = int(prob1.readline())
    dic = {}
    if n==0:
        answers.append('INSOMNIA')
    #print answers
    for j in xrange(1,25*n):
        numbers = list(str(j*n))
        for k in numbers:
            if k not in dic.keys():
                dic[k]=1
        l = dic.keys()
        l.sort()
        #print l
        if len(l)==10 :
            answers.append(str(j*n))
            break
        #print answers
prob1.close()

sol1 = open('sol1.txt','w')
for i in range(len(answers)):
    sol1.write('Case #'+str(i+1)+': '+answers[i]+'\n')