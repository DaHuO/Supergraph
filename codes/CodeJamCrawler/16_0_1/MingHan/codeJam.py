def divideAndDump(digit_set, n):
    while n:
        digit_set.add(n%10)
        n/=10

def countSheep(n):
    if n==0:
        return "INSOMNIA"
    #memo = []
    digits = set()
    divideAndDump(digits, n)
    #memo.append(n)
    count = 1
    current_num = count*n

    while True:
        if len(digits)==10:
            return str(current_num)
        else:
            count += 1
            current_num = count*n
            divideAndDump(digits, current_num)

if __name__=="__main__":
    fin = open("A-large.in")
    fout = open("large_result.txt","w")
    T = int(fin.readline().strip())
    for i in range(T):
        N = int(fin.readline().strip())
        result = countSheep(N)
        fout.write("Case #"+str(i+1)+': '+result+'\n')
    fin.close()
    fout.close()