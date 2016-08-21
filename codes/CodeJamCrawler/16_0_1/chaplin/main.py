def problem_2016A():
    t=int(raw_input())
    for case in range(1,t+1):
        N=int(raw_input())
        if N==0:
            print 'Case #' + str(case) + ': ', 'INSOMNIA'
        else:
            a = [0 for i in range(10)]
            k = 1
            while True:
                M = k * N
                while M > 0:
                    a[M%10] = 1
                    M = M/10
                if 0 not in a:
                    print 'Case #' + str(case) + ': ', N*k
                    break
                k = k + 1
        

def main():
    problem_2016A()
    
if __name__ == '__main__':
    main()
