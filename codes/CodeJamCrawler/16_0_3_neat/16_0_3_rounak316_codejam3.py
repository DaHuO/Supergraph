
from functools import reduce
from itertools import permutations
from math import sqrt

with open("C:\\Users\\prakhar\\Downloads\\C-small-attempt0.in") as f:
    lines = f.readlines()
def _input():
    return lines.pop(0).rstrip('\n')





def perm(N , len , pos):


    if len == pos:
        yield ('1' + N + '1')

    else:
        yield from perm(N + ('0') , len , pos+1)
        yield from perm(N + ('1') , len, pos+1)



def factors(n):
    for i in range( 2, int(sqrt(n )) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            return str(i)



def perms(len:int):
    len = len - 2
    yield from perm('' , len , 0)

def trivialFactors(N):
    return factors(N)


OUT = ""

T = input()
for p in range (int(T)):
    OUT+= "Case #" +str(p+1) + ":\n"
    st = input()
    _nos = st.split()
    a = int(_nos[0])
    b = int(_nos[1] )
    counter = 0
    for _i in perms(a):
        TMP = ''
        TMP += (_i + " ")
        for i in range(2,11):

            X = ( int(_i , i) )
            RES = trivialFactors(  X  )
            if RES is None:

                break

            TMP += ( RES  + " ")
        else:
            counter =counter + 1
            OUT+= TMP + '\n'
            if counter==b:
                break



with open("JAM3.out" , 'w') as fle:
    fle.write(OUT)










