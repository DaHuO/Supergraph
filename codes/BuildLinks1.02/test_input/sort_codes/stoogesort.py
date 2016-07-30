import random

def stoogesort(seq,i,length):
    if seq[length] < seq[i]:
        a,b = seq[length], seq[i]
        seq[i], seq[length] = a,b
    if (length-i +1) >= 3 :
        t = (length - i + 1) /3
        stoogesort(seq, i, length-t)
        stoogesort(seq, i+t, length)
        stoogesort(seq, i, length-t)
    return


def main():
    sort_me = [random.randint(0,100) for x in range(0,100)]

    print "Before %s\n"%sort_me
    #
    stoogesort(sort_me)

    print "After %s\n"%sort_me

if __name__=="__main__":
    main()

