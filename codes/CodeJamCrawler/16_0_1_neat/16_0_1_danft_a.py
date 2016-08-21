import sys;
t=int(input());

for tt in range(0,t):
    n=int(input());
    sys.stdout.write('Case #{}: '.format(1+tt));

    q=set();
    if n==0:
        print("INSOMNIA");
        continue;

    for y in str(n):
        q.add(int(y));
    N=n;

    k=0;
    while k<1000000 and len(q) < 10:
        n+=N;
        for y in str(n):
            q.add(int(y));
        k+=1;
    if(len(q) < 10):
        print("INSOMNIA");
    else:
        print(n);
        

    

