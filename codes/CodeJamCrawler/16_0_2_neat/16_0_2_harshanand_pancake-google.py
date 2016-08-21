def pancake(n):
    n = n.rstrip('+')
    if n == '':
        return 0
    count = 0
    while n != '':
        if n[0] == '+':
            flag = False
            temp = ''
            for i in n:
                if i == '+' and flag == False:
                    temp += '-'
                else:
                    flag = True
                    temp += i
            count += 1
            # print temp
            n = temp
        if n[0] == '-':
            temp = ''
            n = n.lstrip('-')
            if n == '':
                return count+1
            else:

                for i in n:
                    if i == '+':
                        temp += '-'
                    if i == '-':
                        temp += '+'
                n = temp[::-1]
                count += 1
                # print temp[::-1]

f = open("B-large.in", 'r')
f1 = open("output_pancake.txt", 'w')
noTestcases = int(f.readline())
input = []
for j in range(noTestcases):
    input.append(f.readline().strip())
print input
for i,s in enumerate(input):
    ans = pancake(s)
    f1.write("Case #" + str(i+1) + ": " + str(ans) + "\n")


