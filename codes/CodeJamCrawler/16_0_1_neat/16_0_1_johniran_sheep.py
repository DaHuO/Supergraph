#!/usr/bin/python
import sys

try:
    file_r = open(sys.argv[1],"r")
    items = file_r.readlines()
except:
    print '\nCannot open input file\n'
    exit(1) 

try:
    file_w = open(sys.argv[2],"w")
except:
    print '\nCannot open input file\n'
    exit(1) 

for i in xrange(0,len(items)):
    try:
        if items[i].rfind(r"\n")!=-1:
            items[i] = int(items[i][:items[i].rfind(r"\n")])
        else:
            items[i] = int(items[i])
    except:
        print '\nMaybe the last one\n'
#file_w.write('Input\tOutput\n\n{0}'.format(items[0]))
for j in xrange(1,items[0]+1):
    i = 1
    vet = []
    vet_c = 0
    N = items[j]
    ret = old_ret = ''
    while vet_c<10:
        old_ret = ret
        ret = list(str(i*N))
        #print i*N
        for item in ret:
            if not item in vet:
                vet.append(item)
                #print vet
                vet_c+=1
        if ret==old_ret:
            file_w.write('Case #{0}: INSOMNIA\n'.format(j))
            break
        i+=1
    if ret!=old_ret:
        #print vet
        file_w.write('Case #{0}: {1}\n'.format(j,''.join(ret)))
        
file_w.close()