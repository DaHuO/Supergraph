
T = int(raw_input())
N,J = raw_input().split()
N = int(N)
J = int(J)


if N!=32 or J!=500 or T!=1:
    raise Exception("Unexpected input")

print "Case #1:"

print "1"+"0"*30+"1 3 4 5 6 7 8 9 10 11"

s = int("1"+"0"*30+"1" , 2) 
for i in range(2, 31, 2):
    for j in range(1, 31, 2):
        print "%s 3 4 5 6 7 8 9 10 11" % bin(s+(1<<i)+(1<<j))[2:]

total = 226
for i in range(2, 31, 2):
    if(total == 500):
        break
    for j in range(1, 31, 2):
        if(total == 500):
            break
        for k in range(i+2, 31, 2):
            if(total == 500):
                break
            for l in range(j+2, 31, 2):
                if(total == 500):
                    break
                print "%s 3 4 5 6 7 8 9 10 11" % bin(s+(1<<i)+(1<<j)+(1<<k)+(1<<l))[2:]
                total += 1



