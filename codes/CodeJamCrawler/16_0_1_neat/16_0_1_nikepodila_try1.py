fi = open("small.in","r")
T = int(fi.readline().rstrip('\n'))
fo = open("small.out","w")
for i in range(1,T+1):
    N = fi.readline().rstrip('\n')
    nums = set('')
    flag = 0
    for j in range(1,100):
        num = str(j*int(N))
        nums = nums.union(set(num))
        if len(nums) == 10:
            flag = 1
            break
    if flag == 1:
        fo.write('Case #'+str(i)+': '+str(num)+'\n')
    else:
        fo.write('Case #'+str(i)+': INSOMNIA'+'\n')
fo.close()
fi.close()
