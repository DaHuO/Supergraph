case=[]
with open('/Users/cindy_liao/Downloads/A-large.in','r') as file1:
    case_num=file1.readline()
    case=file1.readlines()
for i in range(int(case_num)):
    case[i]=int(case[i].strip())



def count_sheep(n):

    if n==0:
        return 'INSOMNIA'
    else:
        count=1
        num=n
        digits=[0,1,2,3,4,5,6,7,8,9]
        while True:
            for i in str(num):
                if int(i) in digits:
                    digits.remove(int(i))

            if digits==[]:
                return num
            else:
                count+=1
                num=count*n




for i in range(len(case)):
    with open('/Users/cindy_liao/Desktop/1.txt','a') as file2:
        file2.write('Case #'+str(i+1)+': '+str(count_sheep(case[i]))+'\n')

'''

with open('/Users/cindy_liao/Desktop/1.txt','a') as file2:
        file2.write(str(i)+'\n')
'''