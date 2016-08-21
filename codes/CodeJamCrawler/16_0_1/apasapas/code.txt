def A(N):
    try:
        N = int(N)
        if N == 0:
            return 'INSOMNIA'
        remaining_digits = '0123456789'
        s = str(N)
        mult = 1
        while remaining_digits:
            s = str(mult * N)
            remaining_digits = ''.join([i for i in remaining_digits if i not in s])
            mult += 1
        return s
    except TypeError:
        return 'WRONG TYPE: input is ', type(N), 'instead of int'
    