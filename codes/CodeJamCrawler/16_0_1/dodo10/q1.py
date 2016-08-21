#!/usr/bin/python

def main():
    xx = int(raw_input())

    for i in range(1,xx+1):
        res = "Case #" + str(i) + ": " 
        digits = set()
        N = int(raw_input())
        if N == 0:
            print res + "INSOMNIA"
        else:
            # Check muiltiples of N
            j = 1
            while True:
                cn = N * j
                digits.update(set(str(cn)))
                #print digits
                if len(digits) >= 10:
                    break

                j += 1

            print res + str(cn)

if __name__ == "__main__":
    main()
