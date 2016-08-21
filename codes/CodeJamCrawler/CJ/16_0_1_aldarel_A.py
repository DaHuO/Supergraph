
def is_dict_full(dict):
    result = True
    for i in range(0,10):
        if i in dict.keys():
            result = result and True
        else:
            result = False
    return result


if __name__ == '__main__':
    t = int(input())
    for j in range(1, t+1):
        n = int(input())
        if n == 0:
            print('Case #%s: INSOMNIA' % str(j))
            continue
        i = 1
        digit_dict = dict()
        while not is_dict_full(digit_dict):
            curr_num   = i*n
            digit = 1
            while digit <= curr_num:
                digit_dict[(curr_num//digit)%10] = True
                digit = digit*10
            i = i + 1
        print('Case #%s: %s' % (str(j), str(curr_num)))