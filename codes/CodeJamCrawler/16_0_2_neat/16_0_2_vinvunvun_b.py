f = open('b.txt', 'r')
output = open('br.txt','w')

f.readline()
result = []

def trim_happy(s):
    t = len(s)
    for i in xrange(t):
        if(s[t-1-i] == '+'):
            s = s[:-1]
        else:
            break
    return s

result = []

for line in f.readlines():
    s = line.strip()
    s = trim_happy(s)
    t = 0
    print("-----------------")
    while len(s) > 0:
        if(s[0] == '-' and s[-1] == '-'):
            tmp_s = list(s[::-1])
            for i in xrange(len(s)):
                if tmp_s[i] == '-':
                    tmp_s[i] = '+'
                else:
                    tmp_s[i] = '-'
            s = ''.join(tmp_s)
        else:
            "begin +, end -"
            tmp_s = list(s[::-1])
            for i in xrange(len(s)):
                if tmp_s[i] == '+':
                    tmp_s[i] = '-'
                else:
                    break
            s = ''.join(tmp_s)

        t+= 1
        s = trim_happy(s)

    print("result: " + str(t))
    result.append(t)

print result
i = 1
for r in result:
    output.write("Case #"+ str(i) + ": " + str(r) + "\n")
    i += 1
