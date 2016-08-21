def get_last_index_from_head(s, target):
    '''
    >>> '---++---', '+'
    4
    >>> '---++---', '-'
    2
    >>> '--+', '+'
    2
    '''
    neg_target = '+' if target == '-' else '-' 
    idx_tmp = s.find(target)
    if s[idx_tmp:].find(neg_target) != -1:
        return idx_tmp + s[idx_tmp:].find(neg_target) - s[idx_tmp:].find(target) - 1
    else:
        return len(s) - s[idx_tmp:].find(target)

def Revenge_of_the_Pancakes(case):
    n = raw_input()
    count = 0
    while True:
        if len(n) == 0 or n.find('-') == -1: #'', '---'
            break

        idx = get_last_index_from_head(n, '+')

        if idx == -1: #'---'
            count = count+1
            break
        elif n.find('+') == 0: #'+...'
            n = n[idx+1:]
            if n.find('-') != -1:
                count = count+1
        else: #'-...'
            n = n[idx+1:]
            count = count+1
            if n.find('-') != -1 :
                count = count+1

    ans = count

    print "Case #" + str(case) + ": " + str(ans)



if __name__ == "__main__":
    cases = input()
    for case in range(1,cases+1):
        Revenge_of_the_Pancakes(case)
