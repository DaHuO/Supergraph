n = int(input())

for q in range(1,n+1):
    pan = input()
    flip = 0
    for i in range(1,len(pan)):
        if pan[i] != pan[i-1]:
            flip += 1
    if pan[-1] == '-' :
        result = flip + 1
    if pan[-1] == '+' :
        result = flip
    print("Case #" + str(q) + ": " + str(result))
