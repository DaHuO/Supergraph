import math
sushu = open("sushu.txt")
prime = []

def gao(biform):
    global prime
    ans = []
    for i in range(2, 11):
        num = int(biform, i)
        get = False
        for x in prime:
            if(x * x > num):    break
            if(num % x == 0):
                get = True
                ans.append(x)
                break
        if not get:return None
    return ans



def main():
    global prime
    fhan = open("small.in")
    out = open("out.txt", "w")
    Pri = open("sushu.txt")
    for pri in Pri:
        prime.append(int(pri))
    print('make prime done!')

    tc = 1
    firstline = True
    prim = dict()


    for line in fhan:
        if(firstline == True):
            firstline = False
            continue
        n = int(line.split(' ')[0])
        J = int(line.split(' ')[1])

        start = int('1'+'0'*(n-2)+'1', 2)
        end = start + 2
        #end = int('1'*n, 2)
        #print bin(start)
        #print start, end

        getcnt = 0
        while getcnt < J:
            temp = bin(start).replace('0b','')
            start += 2

            #print temp
            ans = gao(temp)
            if(ans == None) :

                continue
            else :
                print getcnt, temp
                out.write(temp)
                for item in ans:
                    out.write(' ' + str(item))
                getcnt += 1
                out.write('\n')


if __name__ == '__main__':
    main()