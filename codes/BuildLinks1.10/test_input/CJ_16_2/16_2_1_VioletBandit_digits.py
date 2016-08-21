f = open('input.txt', 'r')
fout = open('output.txt', 'w+')
nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
total = int(f.readline())
s2 = ""
for k in range(total):
    dict = {}
    lis = []
    sen = f.readline()
    #print sen
    for ch in sen:
        if not dict.has_key(ch):
            dict[ch] = 1
        else:
            dict[ch] += 1
    num = 0
    for ch2,n in [('Z', 0), ('W', 2), ('U', 4), ('X', 6), ('G', 8)]:
        if dict.has_key(ch2):
            num = dict[ch2]
            for i in range(num):
                lis.append(n)
                for ch in nums[n]:
                    dict[ch] -= 1
    for ch2, n in [('O', 1), ('R', 3), ('F', 5), ('S', 7)]:
        if dict.has_key(ch2):
            num = dict[ch2]
            for i in range(num):
                lis.append(n)
                for ch in nums[n]:
                    dict[ch] -= 1
    for ch2, n in [('I', 9)]:
        if dict.has_key(ch2):
            num = dict[ch2]
            for i in range(num):
                lis.append(n)
                for ch in nums[n]:
                    dict[ch] -= 1
    lis.sort()
    s = ""
    for i in lis:
        s+="%d" %i
    s2 += "Case #%d: " %(k+1) + s
    s2 += '\n'

    #print lis
fout.write(s2)
f.close()
fout.close()