import sys

def pancakes(string):

    if('-' not in string):
        return(0)

    elif('+' not in string):
        return(1)
        
    else:
        num = 0;
        while('-' in string):

            if('+' not in string):
                 string = len(string)*'+'
                 num += 1
                 return(num)
            
            plus = string.index('+')
            minus = string.index('-')

            if(plus < minus):
                string = len(string[:minus])*'-' + string[minus:]
                num += 1
            else:
                string = len(string[:plus])*'+' + string[plus:]
                num += 1

        return(num)


if __name__ == "__main__":
    f = sys.stdin
    t = int(f.readline())
    arr = dict()
    for i in range(1,t+1):
        line = f.readline().strip()
        arr[i] = pancakes(line)
    for j in arr:
        print("Case #%d: %d" % (j,arr[j]))
