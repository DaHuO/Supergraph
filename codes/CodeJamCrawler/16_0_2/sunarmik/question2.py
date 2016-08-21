import re
def flip(seq,nums):        
        if seq[0]=='+':
            for i in range(nums):
                seq[i]='-'
        else:
            for i in range(nums):
                seq[i]='+'
        #print 'after modification'
        #print seq
def getSteps(str1):
    chars=re.findall(r"[-+]",str1)
    #print chars
    counter=0
    while True:
        if len(set(chars))<=1 and chars[-1]=='+':            
            break
        elif len(set(chars))<=1 and chars[-1]=='-':
            flip(chars,len(chars))
            counter=counter+1
            break
        temp=chars[0]
        nums=0
        for ch in chars:
            nums=nums+1
            new_list=[]
            if ch!=temp:
                #new_list=[chars[x] for x in range(nums)]
                flip(chars,nums)                
                break
            else:
                temp=ch
        counter=counter+1
    return counter
T=int(raw_input())
for i in range(0,T):
        s=str(raw_input())
        num=getSteps(s)
        print 'Case #%d: %d'%(i+1,num)
