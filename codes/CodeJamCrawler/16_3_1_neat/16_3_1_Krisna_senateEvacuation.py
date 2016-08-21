INPUT  = "A-large.in"
OUTPUT = "A-large.out"

def solve(n,l):
    t=sum(l)
    ans=''
    while t>0:
        max_in=[]
        max_val=max(l)
        for i in xrange(n):
            if l[i]==max_val:
                max_in.append(i)
                if len(max_in)==2: break

        if max_val>1:
            if len(max_in)==2:
                ch1=chr(max_in[0]+ord('A'))
                ch2=chr(max_in[1]+ord('A'))
                ans+=ch1
                ans+=ch2
                ans+=' '
                t-=2
                l[max_in[0]]-=1
                l[max_in[1]]-=1

            else:
                ch1=chr(max_in[0]+ord('A'))
                ans+=ch1
                ans+=ch1
                ans+=' '
                t-=2
                l[max_in[0]]-=1
                l[max_in[0]]-=1

        else:
            if t==2:
                ch1=chr(max_in[0]+ord('A'))
                ch2=chr(max_in[1]+ord('A'))
                ans+=ch1
                ans+=ch2
                t-=2
                l[max_in[0]]-=1
                l[max_in[1]]-=1

            else:
                ch1=chr(max_in[0]+ord('A'))
                ans+=ch1
                ans+=' '
                t-=1
                l[max_in[0]]-=1

    return ans

with open(INPUT) as infile:
    with open(OUTPUT, 'w') as outfile:
        t = int(infile.readline())

        for i in xrange(t):
            n = int(infile.readline())
            line = infile.readline()
            inputVal = [int(x) for x in line.strip().split()]
            #print solve(n,inputVal)#,"ASDG"
            ans=solve(n,inputVal)
            #print inputVal[0],inputVal[1]
            print "Case #%d: %s" % (i + 1,ans)
            outfile.write("Case #%d: %s\n" % (i + 1,ans))