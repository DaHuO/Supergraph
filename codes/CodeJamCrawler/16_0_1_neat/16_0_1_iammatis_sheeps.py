import sys

def sheeps(number):

    if(number == 0): return(None)

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    arr = []

    mult = 1
    while(len(arr) != 10):
        num = number * mult
        for i in str(num):
            if(i not in arr):
                arr.append(i)
        mult += 1
        
    return(num)

if __name__ == "__main__":
    f = sys.stdin
    t = int(f.readline())
    arr = dict()
    for i in range(1,t+1):
        line = f.readline().strip()
        arr[i] = sheeps(int(line))
    for j in arr:
        if(arr[j] is None):
            print("Case #%d: %s" % (j,'INSOMNIA'))
        else:
            print("Case #%d: %d" % (j,arr[j]))
