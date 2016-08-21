def return_digits(n):
    return_list=[]
    while(n!=0):
        return_list.append(n%10)
        n=n/10
    return return_list
def match(list_1, list_2):
    if len(set(list_1))==len(set(list_2)):
        c=0
        for i in list(set(list_1)):
            if i in list(set(list_2)):
                c+=1
        if c==len(set(list_1)):
            return True
    return False
def sheep_sleep(n):
    l=[1,2,3,4,5,6,7,8,9,0]
    i=n
    ans_list=[]
    while True and n>0:
        ans_list=ans_list+return_digits(i)
        if match(l, ans_list):
            return i
            break
        i=i+n
    return "INSOMNIA"
x=input()
res_list=[]
for i in range(x):
    i=input()
    res_list.append(sheep_sleep(i))
for i in range(0, len(res_list)):
    print "Case #"+str(i+1)+": "+str(res_list[i])  
    
        
        
    


