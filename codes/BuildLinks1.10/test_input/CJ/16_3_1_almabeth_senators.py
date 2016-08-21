import numpy as np
import string

testfile='A-large.in'
outputfile='A-large.out'
#outputfile='A-small-attempt0.out'

fo = open(testfile, "rw+")
print "Name of the file: ", fo.name
firstline = fo.readline()

numcases=int(firstline.split('\n')[0])
print 'numcases: ',numcases

d = dict(enumerate(string.ascii_uppercase, 1))


def evacuate(Nparties,peoplestart):
    Npeople=np.sum(peoplestart)
    people=np.array(peoplestart)
    out=''
    for i in np.arange(Npeople):
        if np.sum(people)==0:continue
        #print people
        remove=np.zeros_like(people)
        diff=np.abs(np.diff(people))
        if np.sum(people)==2:
            args=np.transpose(np.argwhere(people!=0))[0]
            remove[args]=1
            leave=''
            for arg in args:
                leave=leave+d[arg+1]            
        elif np.sum(diff)==0:
            args=np.transpose(np.argwhere(people!=0))[0]
            if np.size(args)>2:
                args=[args[2]]
            remove[args]=1
            leave=''
            for arg in args:
                leave=leave+d[arg+1]
                   
        else:
            arg=np.argmax(people)
            remove[arg]=1
            leave=d[arg+1]
        #print leave     
        people=people-remove
        assert np.sum(people)/2.0>=np.max(people)
        #args= map(int,np.argwhere(remove==1))
        #leave=''
        #for arg in args:
            #leave=leave+d[arg+1]
        #print leave
        out=out+' '+leave
    return out


outfile=open(outputfile, 'w')
for case in np.arange(1,numcases+1): 
    print '********'+str(case)+'********'
    Nparties=int(fo.readline().split('\n')[0])
    people=map(int,fo.readline().split('\n')[0].split(' '))
    answer=evacuate(Nparties,people)
    print answer
    outfile.write('Case #'+str(case)+': '+str(answer)+'\n')
    
outfile.close()
fo.close()
print 'Done.'

b=2
