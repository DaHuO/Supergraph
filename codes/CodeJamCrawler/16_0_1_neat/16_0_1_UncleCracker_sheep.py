'''
Created on Apr 9, 2016

@author: christoph
'''


def main():  
    T = int(raw_input())
    for i in range(T):
        digits = set()
        n = int(raw_input())
        if n == 0:
            print "Case #" + str(i+1) + ": INSOMNIA"
            continue
        out = 0
        j = 1
        while True:
            if len(digits) == 10:
                break
            tmp = n*j
            out = tmp
            j += 1
            while tmp:
                digits.add(tmp%10)
                tmp /= 10
        print "Case #" + str(i+1) + ": " + str(out)


if __name__ == "__main__":
    main()