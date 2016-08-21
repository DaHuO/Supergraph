from random import choice

def convert(digits,base):
    n=0
    for i,d in enumerate(digits):
       n=n*base+d
    return n


def factor(n):
    for p in range (2,min(1000,int(n**0.5)+2)):
        if n%p==0:
            return p
    return 0

def jamcoin(digits):
    ans=[]
    for b in range(2,11):
        n=convert(digits,b)
        f=factor(n)
        if f==0:
            return False
        else:
            ans.append(f)
    return ans
    


def randomdigits(N):
    ans=[1]
    for i in range(N-2):
        ans.append(choice([0,1]))
    ans.append(1)
    return ans


def process(N,J,filename):

    lines=[]

    answers={}
    for i in range(100000):
        d=randomdigits(N)
        key=convert(d,2)
        if not(key in answers):
            j=jamcoin(d)
            if j:
                answers[key]=(d,j)
        if len(answers)==J:
            break

    for k in answers:
        (d,j)=answers[k]
        out= ''.join(map(str,d)) + ' ' + ' '.join(map(str,j))
        lines.append(out)

    outfile=open("C:\\Users\\Jon\\Dropbox\\0_codejam2016\\Qual_C\\"+filename,"w")

    outfile.write("Case #1:\n")

    outfile.write('\n'.join(lines))
    outfile.close()


process(16,50,"c_out_small.txt")
process(32,500,"c_out_large.txt")
