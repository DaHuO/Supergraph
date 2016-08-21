def doer(N):
    temp = N
    num_list = list(set(list(str(temp))))
    if N==0:
        return "INSOMNIA"
    while True:
        if(len(num_list)==10):
            return temp
        temp+=N
        num_list = list(set(num_list + list(str(temp))))


if __name__=='__main__':
    T = input()
    for i in range(T):
        print 'CASE #{0}: {1}'.format(i+1, doer(input()))