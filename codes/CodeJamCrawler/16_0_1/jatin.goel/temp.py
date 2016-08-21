'''
    ------------------------------------------------------------------------------------------------------------------------------------------
    ##########################################################################################################################################
    ------------------------------------------------------------------------------------------------------------------------------------------
'''

def A():
    '''
        Google Code Jam
        Year 2016
        Problem A
    '''
    f = open(r'C:\Users\Jatin\Downloads\A-large.in', 'r')
    output = open(r'C:\Users\Jatin\Downloads\A-large-result.txt', 'w')
    cases = int(f.readline())
    for case in range(cases):
        result = 'Case #' + str(case + 1) + ': '
        N = f.readline().split()[0]
        print N
        if N == '0':
            result += 'INSOMNIA'
        else:
            original = range(10)
            x = map(int, list(N))
            original = list(set(original) - set(x))
            i = 2
            while original:
                A = str(int(N) * i)
                x = map(int, list(A))
                original = list(set(original) - set(x))
                i += 1
            result += str(A)
        output.write(result + '\n')
    output.close()
    f.close()

A()