input_fil = open('A-large.in','r')
with open('outfile.out', 'w') as outfile:
    n=int(input_fil.readline())
    for j in range(0,n):
        num=input_fil.readline()
        l=[]
        i=1
        flag=0
        while(len(l)!=10):
            val1=str(i*int(num))
            i=i+1
            val=val1
            val1=list(val1)
            if (i==100000):
                print >>outfile,'case #'+str(j+1)+':','INSOMNIA'
                flag=1
                break
            for x in val1:
                if x not in l:
                    l.append(x)
        if (flag==0):
            print >>outfile,'case #'+str(j+1)+':',val        
    
'''
this is code for Problem A. Counting sheep
code tested and verified in python 2.7.11
Operating system tested in :Windows 10 64 bit machine
NOTE: dosent work in python 3 and above because print statement has become a function
the input file is to be placed in the same direcoty as the code
the code file is of the format filename.py
the output is generated in a filename.out file
the length of the code is 22 lines
'''
