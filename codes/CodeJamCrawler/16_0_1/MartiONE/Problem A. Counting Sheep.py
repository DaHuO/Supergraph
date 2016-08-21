from sys import stdin
def chk(case):
    result = [0,1,2,3,4,5,6,7,8,9]
    count = 0
    while len(result) > 0:
        count += 1
        [result.pop(result.index(int(i))) for i in str(case*count) if int(i) in result]
    return count

def read():
    return stdin.readline()

for n in range(int(read())):
    num = int(read())
    if num == 0:
        print("Case #{}: INSOMNIA".format(str(n+1)))
    else:
        print("Case #{}: {}".format(str(n+1), num*chk(num)))
   
        