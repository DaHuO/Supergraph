def int_in_base(n, b):
    n_str = str(n)
    n_len = len(n_str)
    multi = 1
    result = 0
    for i in range(n_len-1,-1,-1):
        result += int(n_str[i]) * multi
        multi = multi * b
    return result
