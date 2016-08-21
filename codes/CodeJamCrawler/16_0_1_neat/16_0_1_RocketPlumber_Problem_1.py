__author__ = 'shant_000'

def all_digits_seen(diglist):
    for x in range(0, 10):
        if x not in diglist:
            return False
    return True


t = int(input())
#t = 1000000
for i in range(1, t+1):
    n = int(input())
    #n = i
    if n == 0:
        print("Case #" + str(i) + ": INSOMNIA")
    else:
        digs = []
        m = 0
        while(True):
            m+=1
            test_this = str(n*m)
            for a_dig in test_this:
                if int(a_dig) not in digs:
                    digs.append(int(a_dig))
            if all_digits_seen(digs):
                print("Case #" + str(i) + ": " + str(test_this))
                break