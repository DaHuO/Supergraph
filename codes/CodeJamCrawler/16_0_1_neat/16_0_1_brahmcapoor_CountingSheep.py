t = int(input())
for i in range(1,t+1):
    digits = {0,1,2,3,4,5,6,7,8,9}
    number = int(input())
    offset = number
    if (number == 0):
        print(("Case #{}: INSOMNIA").format(i))
        continue
    while(len(digits) != 0):
        nString = str(number)
        for ch in nString:
            digits.discard(int(ch))
        number += offset
    print(("Case #{}: {}").format(i,number-offset))
