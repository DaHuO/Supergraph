
def ret_digits(n):
    n = str(n)
    digits = list(n)
    return digits

def check_all(all):
    stat = False
    for i in range(10):
        if str(i) in all:
            stat = True
        else:
            stat = False
            break

    return stat

n = int(raw_input())

for i in range(n):
    N = int(raw_input())
    if N == 0:
        print "Case #"+str(i+1)+": INSOMNIA"
    else:
        all_digits = ret_digits(N)
        j=1
        while True:
            if check_all(all_digits):
                print "Case #"+str(i+1)+": "+str(final)
                break

            j = j+1
            final = N*j
            all_digits.extend(ret_digits(final))
            all_digits = list(set(all_digits)) 
