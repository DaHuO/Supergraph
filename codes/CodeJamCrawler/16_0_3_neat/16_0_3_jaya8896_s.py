def count(st):
    val = 0
    for it in st:
        if it=='1':
            val += 1
    return val
dic = {}
t = input()
n,k = map(int,raw_input().split())
for i in range(2**14):
    st = bin(i)[2:]
    st = '0'*(14-len(st)) + st + '1'
    st = '1' + st
    arr = []
    #print st
    #print len(dic)
    st_rev = st[::-1]
    for i in range(2,11):
        val = 0
        for j in range(16):
            if st_rev[j]=='1':
                val += i**j
        fl = False
        if i%2:
            ones = count(st)
            if ones%2==0:
                arr.append(2)
                fl = True
            else:
                break
        else:
            if val%3==0 or val%5==0 or val%7==0:
                fl = True
                if val%3==0:arr.append(3)
                elif val%5==0:arr.append(5)
                elif val%7==0:arr.append(7)
            else:
                break
        if not fl:
            break
    if len(arr)==9:
        dic[st] = arr
    if len(dic)>=50:
        break
print "Case #1:"
for item in dic:
    print item,
    print " ".join(map(str,dic[item]))
