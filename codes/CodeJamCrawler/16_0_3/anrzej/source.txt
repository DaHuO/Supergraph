
start = int(0b1000000000000001)
ans = []
for i in range(start, start*10):
    tans = []
    if(len(ans) == 50):
        break
    for b in range(2, 11):
        num = int(str(bin(i))[2:], b)
        for j in range(2, 8):
            if num % j == 0:
                tans.append(j)
                break
    if len(tans) == 9 and str(bin(i))[-1] == '1':
        ans.append((bin(i), tans))

print("Case #1:")
for i in ans:
    print(str(i[0][2:]), ' '.join(str(a) for a in i[1]))