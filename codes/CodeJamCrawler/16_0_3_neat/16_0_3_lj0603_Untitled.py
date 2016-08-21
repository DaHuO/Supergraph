
# coding: utf-8

# In[136]:

infile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\3\\C-small-practice.in.txt', 'r')
outfile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\3\\result.txt', 'w')
N=int(infile.readline())
x=infile.readline()
index_blank=0
for j in range(4):
    if x[j]==' ':
        index_blank=j
        break
L=int(x[0:index_blank])
n=int(x[index_blank:])
outfile.write('case #1: \n')
count=0
for i in range(0b1000001000111111,0b1111111111111111,0b10):
    divisor=[]
    for j in range(2,11):
        n=int(str(bin(i))[2:18],j)
        for k in range(2,int(n/2)+1):
            if n%k==0:
                divisor.append(k)
                break
            else:
                continue
        else:
            break
    if(len(divisor)==9):
        outfile.write(str(bin(i))[2:18])
        for j in range(9):
            outfile.write(' '+str(divisor[j]))
        outfile.write('\n')
        count+=1
        if count<=4:
            continue
        else:
            break
    else:
        continue
infile.close()
outfile.close()


# In[ ]:



