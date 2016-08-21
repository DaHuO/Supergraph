# trait inheritence

# LGL
# LGL  GGG  LGL
# 0->0,1,2
# 1->3,4,5,   1,  7
# 2->6,7,8

# if S>=T
# choosing


t=2
k=1
s=3



file=open("D-small-attempt1.in","r")
file_out=open("D.out","wr")



case_n=int(file.readline())

for case_id in xrange(case_n):
    case_v=file.readline().split(" ")
    t=int(case_v[0])
    k=int(case_v[1])
    s=int(case_v[2])

    if k==1:
        if s>=t:
            file_out.writelines("Case #"+str(case_id+1)+":")
            for x in range(1,t+1):
                file_out.writelines(" "+str(x))
            file_out.writelines("\n")
        else:
            file_out.writelines("Case #"+str(case_id+1)+": IMPOSSIBLE\n")
    elif s==t:
        file_out.writelines("Case #"+str(case_id+1)+":")
        for x in range(1,t+1):
            file_out.writelines(" "+str(x))
        file_out.writelines("\n")
    else:
        sets=[]
        # try each combination that only one digit is 1
        for x in xrange(0,t):
            sets.append(str(bin(pow(2,x)))[2::])
        #
        # for x in xrange(0,pow(2,t)):
        #     sets.append(str(bin(x))[2::])

        for index in xrange(len(sets)):
            while len(sets[index])<t:
                sets[index]="0"+sets[index]

        allone=''
        for x in xrange(len(sets[0])):
            allone+='1'


        analysis=[]
        for number in sets:
            origin=number
            count=0
            current=origin
            while count<1 and count<=k-1:
                result=[]
                for bit in xrange(len(current)):
                    if current[bit]=='0':
                        result.append(origin)
                    else:
                        result.append(allone)
                next_generation=''.join(result)
                if count==0:
                    analysis.append(next_generation)
                current=next_generation
                count+=1

        dict={}

        def findCommonOne(A,B):
            result=[]
            for index in xrange(len(A)):
                if A[index]=='1' and B[index]=='1':
                    result.append(index)
            return result

        for x in xrange(len(analysis)-1):
            dict[x]=findCommonOne(analysis[x],analysis[x+1])
        final_result=[]
        for y in xrange(len(analysis)-1):
            if len(dict[y])==0:
                print "None"
            else:
                final_result.append(dict[y][0]+1)

        print final_result
        if len(final_result)>0:
            file_out.writelines("Case #"+str(case_id+1)+":")
            for a in final_result:
                file_out.writelines(" "+str(a))
            file_out.writelines("\n")
        else:
            file_out.writelines("Case #"+str(case_id+1)+": IMPOSSIBLE\n")