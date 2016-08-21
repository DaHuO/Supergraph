import sys
T = int(raw_input())
results=[]
for case in xrange(T):
    N = int(raw_input())
    if N == 0:
        results.append('Case #'+str((case+1))+': INSOMNIA')
        continue
    seen = set()
    for i in xrange(1, sys.maxint):
        multiple = i * N
        digits = [char for char in str(multiple)]
        #print digits
        done = False
        for num in digits:
            #print seen
            seen.add(num)
            if len(seen) == 10:
                results.append('Case #'+str((case+1))+': '+str(multiple))
                done = True
                break
        if done :
            break
#for answer in results:
#    print answer
with open('counting_sheep_small_out.txt', 'w') as f:
    for s in results[:-1]:
        f.write(s)
        f.write("\n")
    f.write(results[-1])



