k = int(input())

p = [ "TWO","EIGHT", "ZERO", "FOUR", "SIX", "SEVEN", "FIVE", "NINE", "ONE", "THREE"]
r = [2,8,0,4,6,7,5,9,1,3]
for i in range(k):
    number = input()
    val = 0
    print("Case #" + str(i + 1), end=": ")
    ans = []
    #print()
    for a in p:
        x = True
        #print(a)
        #print(number)
        while True:
            tmp2 = number

            for s in range(len(a)):
                #print(tmp2)
                if tmp2.count(a[s]) <= 0:
                    x = False

                else:
                    tmp = list(tmp2)
                    tmp.remove(a[s])
                    tmp2 = "".join(tmp)
            if x == True:
                number = "".join(tmp2)
                ans.append(str(r[val]))
            else:
                break
        val += 1
    ans = sorted(ans)
    print("".join(ans))

