# problem 11024
"""
n = int(raw_input())
for i in range(n):
    print sum(map(int, raw_input().split()))
"""
# problem 1002
"""
a = []
for i in range(input()):
    a.append(map(int,raw_input().split()))

    d = pow(a[i][0]-a[i][3],2) + pow(a[i][1]-a[i][4],2)
    x = pow(a[i][2]+a[i][5],2)
    y = pow(a[i][2]-a[i][5],2)

    if d == 0 and a[i][2] == a[i][5]:
        print -1
    elif x == d or y == d:
     print 1
    elif x < d or y > d:
        print 0
    else:
        print 2
"""
# problem 11718 not done
"""
while(1):
    a = raw_input()
    if len(a) == 0:
        break
    print a
"""
# problem 11066


"""
# problem 11531

cnt = 0

while(1):
    a = raw_input().split()
    if a[0]=='-1':
        break
    if a[2]=='right':
        cnt+=1
"""
"""
# CodeJam #1
digit = [0,0,0,0,0,0,0,0,0,0]

cnt = 1
f = open('A-large.txt','r')
fw = open('A-large.out','w')
T = f.readline()

for i in range(int(T)):
    N = f.readline()
    if not N:
        break
    print N

    while True:
        if int(N) == 0:
            fw.write('Case #'+str(i+1)+': '+'INSOMNIA\n')
            break
        n = int(N)*cnt
        x = 10**(len(str(n))-1)
        #print x
        while x>=1:
            k = n/x
            #print n,k
            n = n-(k*x)
            x = x/10
            if digit[k] == 0:
                digit[k] += 1
        if sum(digit) == 10:
            digit = [0,0,0,0,0,0,0,0,0,0]
            fw.write('Case #'+str(i+1)+': '+str(int(N)*cnt)+'\n')
            cnt = 1
            break
        cnt+=1

f.close()
fw.close()
"""

# CodeJam #2

def pop_stack(stack, bot):
    while stack[bot] == '+':
        stack.pop()
        if bot-1 >= 0:
            bot -= 1
        else:
            break
    return stack

def main():
    f = open('B-large.txt','r')
    fw = open('B-large.out','w')
    T = f.readline()


    for n in range(int(T)):
    #for n in range(1):
        tmp = f.readline()
        stack = []
        for i in range(len(tmp)):
            if tmp[i] == '\n':
                break
            stack.append(tmp[i])

        print stack

        cnt = 0
        plus_cnt = 0
        while True:
            pos = len(stack)
            bot = pos-1

            if not stack:
                print 'stack is empty'
                break

            if pos == 1:
                if stack[0] == '+':
                    break
                else:
                    cnt += 1
                    break

            elif stack[0] == '-' and stack[pos-1] == '-':
                for i in range(pos):
                    if stack[i] == '+':
                        stack[i] = '-'
                    else:
                        stack[i] = '+'
                stack.reverse()
                pop_stack(stack,bot)
                cnt += 1

            elif stack[0] == '+' and stack[pos-1] == '+':
                for i in range(pos):
                    if stack[i] == '+':
                        plus_cnt += 1
                if plus_cnt == pos:
                    break

                i=0
                while stack[i] == '+':
                    if i < bot:
                        i += 1
                    else:
                        break
                for j in range(i):
                    if stack[j] == '+':
                        stack[j] = '-'
                pop_stack(stack,bot)
                cnt += 1

            elif stack[0] == '-' and stack[pos-1] == '+':
                i=0
                while stack[i] == '-':
                    i += 1
                for j in range(i):
                    if stack[j] == '-':
                        stack[j] = '+'
                pop_stack(stack,bot)
                cnt += 1
            elif stack[0] == '+' and stack[pos-1] == '-':
                i=0
                while stack[i] == '+':
                    i += 1
                for j in range(i):
                    if stack[j] == '+':
                        stack[j] = '-'
                stack[0:j].reverse()
                pop_stack(stack,bot)
                cnt += 1

        fw.write('Case #'+str(n+1)+': '+str(cnt)+'\n')
        #print 'Case #'+str(n+1)+': '+str(cnt)+'\n'

    f.close()
    fw.close()


main()

