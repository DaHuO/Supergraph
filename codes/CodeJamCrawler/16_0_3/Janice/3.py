import math

def primeTable():
    table = []
    for i in range(2**16):
        table.append(1)
    table[0] = 0
    table[1] = 0
    for i in range(int(math.sqrt(2**16))):
        if table[i] == 1:
            j = 0
            while i * (i + j) < 2**16:
                table[i * (i + j)] = 0
                j += 1
    prime = []
    for i in range(2**16):
        if table[i] == 1:
            prime.append(i)
    return prime

def base(myArray, base):
    ans = 0;
    index = 0
    for i in myArray:
        ans += i * (base**index)
        index += 1
    return ans

def main():
    myInput = open('C-large.in', 'r')
    myOutput = open('output.txt', 'w')
    T = myInput.readline();
    case = 0
    table = primeTable()
    for data in myInput:
        case += 1
        N, J = map(int, data.split())
        myArray = []
        for i in range(N):
            myArray.append(0)
        count = 0
        ans = []
        for i in range((2**(N-1))+1, 2**N):
            if (i % 2) == 1:
                digit = 0
                while i > 0:
                    if (i % 2) == 1:
                        myArray[digit] = 1
                        i = i - 1
                    i = i / 2
                    digit += 1
            else:
                continue
            ansItem = []
            for j in range(2, 11):
                b = base(myArray, j)
                for k in table:
                    if b != k and (b % k) == 0:
                        ansItem.append(str(k))
                        break
            if len(ansItem) == 9:
                temp = []
                s = ""
                for j in myArray:
                    s = str(j) + s
                temp.append(s)
                for j in ansItem:
                    temp.append(str(j))
                ans.append(temp)
                count += 1
            if count == J:
                break
            for j in range(N):
                myArray[j] = 0
        myOutput.write("Case #" + str(case) + ":\n")
        w = ""
        for i in ans:
            for j in range(10):
                if j != 0:
                    w += " "
                    w += str(i[j])
                else:
                    w += str(i[j])
            myOutput.write(w + "\n")
            w = ""
    myInput.close()
    myOutput.close()

main()
