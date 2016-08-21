import math


def baseN(num,b):
    #print("baseN")
    pow = int(math.log10(num))
    digits = [int(i) for i in str(num)]
    num_base = 0
    for d in digits:
        num_base = num_base + d*math.pow(b,pow)
        pow -= 1

    #print("Num: " + str(num) + " in base: " + str(b) + " = " + str(num_base))
    return int(num_base)

def check_prime(n):
    #print("Checking if num: " + str(n) + " is prime")
    if(n<=1):
        raise Exception("Not prime")
    else:
        if n % 2 == 0:
            return 2
        for i in range(3,n, 2):
            #print("i(="+str(i)+") divided by n" + str(n))
            if (n % i) == 0:
                return i
            else:
                if i > 1000000:
                    return 0

        return 0


if __name__ == "__main__":
    x = int(input())



    for i in range(1,x+1):
        N, J = [int(s) for s in input().split(" ")]
        print("Case #{}:".format(i))
        max = int(math.pow(2, N))


        current_res = 0
        for x in range(max):
            bi=bin(x)[2:].zfill(N)

            #print("Size of bi: " + bi + " is " + str(len(str(bi))))
            if len(str(bi)) == N and bi[N-1] == '1' and bi[0] == '1':
                num = int(bi)
                list_divs = [num]

                valid = True
                for j in range(2, 11):
                    num_in_base = baseN(num, j)

                    div = check_prime(int(num_in_base))
                    if div != 0:
                        #print("div was found: " + str(div))
                        list_divs.append(div)
                    else:
                        #print("no div was found: ")
                        valid = False
                        # check_prime(int(num_in_base))
                        #print(list_divs)

                if valid:
                    print(' '.join(str(n) for n in list_divs))
                    current_res = current_res +1

            if current_res==J:
                break
