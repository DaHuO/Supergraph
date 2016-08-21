fin=open('A-small-attempt0.in')
num_line=fin.readlines()
num_cases=fin.readline()
print(num_cases)

for case in range(1, int(input())+1):
    digits_seen=[0]*10
    num=input(); count=1;
    while sum(digits_seen)!=55 and count!=100:
        num=str(int(num))
        for item in list(num):
            item=int(item)
            if digits_seen[0]==0 and item==0:
                digits_seen[0]=10
            elif digits_seen[item]==0:
                digits_seen[item]=item
            else:
                continue
        count+=1
        if sum(digits_seen)==55:
            continue
        num=str(int(int(num)/(count-1))*count)
    if count==100:
        print('Case #{}: {}'.format(case,'INSOMNIA'))
    else:
        print('Case #{}: {}'.format(case,num))
    
        