fi = open("C-large.in","r")
fo = open("output.txt","w")
primes = [0]*1000001
primes[0]=primes[1]=1;
primeIter = [0]*1000001
count=0
ans=0
for i in range(2,1000001):
    if(primes[i]==0):
        primeIter[count]=i;
        count+=1;
        for j in range(2*i,1000001,i):
            primes[j]=1;
t = int(fi.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    fo.write("Case #{}:\n".format(i))
    n, J = [int(s) for s in fi.readline().split(" ")]  # read a list of integers, 2 in this case
    i =1
    while(i<(1<<(n))):
        if(ans==J):
            break
        pows = [0]*11
        for k in range(2,11):
            pows[k] += pow(k,n-1);
            pows[k] += 1;
        temp = "1"
        for j in range(n-2,0,-1):
            if(i&(1<<j)):
                temp += '1';
                for k in range(2,11):
                    pows[k]+=pow(k,j);
            else:
                temp += '0';
        temp += '1';
        fincheck=True
        div = [0]*11
        for j in range(2,11):
            check=True
            k=0
            while(k<count and pows[j]>primeIter[k]):
                if(pows[j]%primeIter[k]==0):
                    check=False
                    break
                k+=1
            if not check:
                div[j] = primeIter[k]
            else:
                fincheck=False
                break 
        if(fincheck):
            ans+=1
            fo.write("{} {} {} {} {} {} {} {} {} {}\n".format(temp,div[2],div[3],div[4],div[5],div[6],div[7],div[8],div[9],div[10]))
        i+=2