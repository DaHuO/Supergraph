import itertools

def counting(case,num):
    if num==0:
        print("Case #{0}: INSOMNIA".format(case))
        return

    checksum = 0
    seen = set()
    val = 0
    while True:
        if(checksum == 55):
            break
        val += num
        s_val = str(val)
        for i in s_val:
            if i not in seen:
                seen.add(i)
                checksum += int(i)+1
    print("Case #{0}: {1}".format(case,val))
    return

cases = int(input())
for i in range(1,cases+1):
    counting(i,int(input()))
