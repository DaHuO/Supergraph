# codejam2016 qualification round source 1
#
from decimal import Decimal
def count(a):
   i=0;s=" ";
   if a==0:
    return "INSOMNIA"
   while(len(s)-1<10):
     i+=1
     s+=str(i*int(a))
     
     s=''.join(set(s))
    
     
    
   return str((i)*int(a) )
with open('D:\dawood\codejam\codejam\codejam\codejam\codejam2016\qualification\input1.in', 'r+') as fin:
 with open('D:\dawood\codejam\codejam\codejam\codejam\codejam2016\qualification\output1.out', 'w') as fout:
    a = [int(x) for x in fin.readline().split()]  # read first line

    for i in range(a[0]):
     b =fin.readline()
     fout.write("Case #"+str(i+1)+": "+count(int(b))+"\n") 