#!/usr/local/bin/python


f = open ("A-large.in", "rb")
T=int(f.readline())
digits = []
N = 0
meh = 1
def main():
    global meh
    global digits
    global N
    for i in range(T):
        N = int(f.readline())

        poo()
        meh +=1




def reset():
    global digits 
    digits = []
    for i in range(10):
        digits.append(0)






def poo():
    reset()
    global meh
    i = 1
    while(True):
        temp = i*N   
        doot(temp)


        if all_digits_seen():
            print "Case #"+str(meh)+": ",
            print i*N

            break
        i += 1

        if i > 100000:
            print "Case #"+str(meh)+": ",
            print "INSOMNIA"

            break


def all_digits_seen():
    for i in digits:
        if i == 0:
            return False
    return True

def doot(num):
    while (True):
        if num == 0:
            break
        one = num % 10
        num/=10
        digits[one]=1



if __name__ == "__main__":
    main()
