def genLastNum(num):
    s = set()
    finalSet = {0,1,2,3,4,5,6,7,8,9}
    t = 0
    while s != finalSet:
        t += num
        l = [int(x) for x in str(t)]
        s |= set(l)
    return t
no_of_inputs = int(input())
for each in range(0,no_of_inputs):
    cur_num = int(input())
    if cur_num == 0:
        result = 'INSOMNIA'
    else:
        result = genLastNum(cur_num)
    print("Case #" +str(each+1)+ ": " + str(result))
