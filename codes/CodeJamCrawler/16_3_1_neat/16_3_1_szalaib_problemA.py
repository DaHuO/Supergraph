import string
def create_senate(numbers):
    senate={}
    count=0
    for i in range(len(numbers)):
        senate[string.uppercase[i]]=int(numbers[i])
        count=count+int(numbers[i])
    return senate,count
    
def is_senate_good(senate,count):
    for party in senate:
        if senate[party]*2>count:
            return False
    return True
    
def brute_force_solution_smallA(numbers):
    result=''
    good=False
    senate,count=create_senate(numbers)
    while count>0:
        
        for party in senate:
            senate[party]-=1
            count-=1
            if is_senate_good(senate,count):
                result+=party+' '
                if senate[party]==0:
                    del senate[party]
                good=True
                break
            else:
                senate[party]+=1
                count+=1
        else:
            for party1 in senate:
                for party2 in senate:
                    senate[party1]-=1
                    senate[party2]-=1
                    count-=2
                    if is_senate_good(senate,count):
                        result+=party1+party2+' '
                        if senate[party1]==0:
                            del senate[party1]
                        if senate[party2]==0:
                            del senate[party2]
                        good=True
                        break
                    else:
                        senate[party1]+=1
                        senate[party2]+=1
                        count+=2
                if good:
                    break
    return result[:-1]
    
def solve_problemA(fname):
    fin=open(fname,'r')
    flines=fin.readlines()
    fin.close()
    fout=open(fname[:-3]+'.out','w')
    for i in range(2,len(flines),2):
        result=brute_force_solution_smallA(flines[i].split())
        fout.write('Case #'+str(i/2)+': '+result+'\n')
    fout.close()
    
    
    
    