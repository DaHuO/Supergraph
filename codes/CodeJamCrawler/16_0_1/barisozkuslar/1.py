def log10nums(number):
    lst = []
    while number > 0:
        lst.append(number % 10)
        number /= 10
    return lst

def main():        
    t = int(raw_input())  
    for tn in xrange(1, t + 1):
        n = int(raw_input())
        happened = [i for i in range(10)]

        print "Case #{}:".format(tn),

        if n == 0:
            print "INSOMNIA"
        else:   
            k = 1
            while happened:
                for digit in log10nums(k * n):
                    try:
                        happened.remove(digit)
                    except:
                        pass
                k += 1

            k -= 1

            print "{}".format(k * n)


if __name__ == '__main__':
    main()
