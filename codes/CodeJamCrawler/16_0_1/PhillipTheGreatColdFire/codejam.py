def fun(N,digits):
    for i in xrange(1,1000000):
        temp = list(str(N*i))
        if len(digits) == 0:
            return N*(i-1)
        for x in temp:
            try:
                digits.remove(int(x))
            except Exception as e:
                pass
    return "INSOMNIA"

if __name__ == "__main__":
    import fileinput
    ten_digits = [1,2,3,4,5,6,7,8,9,0]
    f = fileinput.input()
    T = int(f.readline())
    print T
    for case in range(1,T+1):
        x = f.readline()
        digits = list(ten_digits)
        answer = fun(int(x),digits)
        print("Case #{0}: {1}".format(case, answer))
