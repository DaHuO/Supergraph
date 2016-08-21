#problem C
from math import sqrt
import random

def is_prime(n):
    i = 2
    while(i<=100):
        if(n%i==0):
            return i
        i = i+1
    return 1

fname = "test"
inf = open(fname, 'r')
ofname = "test_output"
of = open(ofname, 'w')

i=0;

for line in inf:
    if(i==0):
        T = int(line);
        i = i+1;
    else:
        if(i>1):
            of.write("\n");
        of.write("Case #"+ str(i) + ":");
        i = i+1;
        x = line.split()
        N = int(x[0])
        J = int(x[1])
        count = 0   #number of jamcoins found
        jamset = set()
        while(count<J):
            s = ''.join(random.choice('01') for i in range(N-2))
            s = "1" + s + "1"
            if(s.count('1')%2==0):
                if(s not in jamset):
                    jamset.add(s)
                    div = ['1', '2', '1', '2', '1', '2', '1', '2', '1']
                    index = 0
                    while(index<9):
                        if(div[index]=='1'):
                            num = int(s, index+2)
                            flag = is_prime(num)
                            if(flag==1):
                                break;
                            else:
                                div[index] = str(flag)
                        index = index + 1
                    if('1' not in div):
                        s = "\n" + s + " " + " ".join(div)
                        of.write(s)
                        count = count + 1
    if(i>T):
        break;
        
inf.close();
of.close();    