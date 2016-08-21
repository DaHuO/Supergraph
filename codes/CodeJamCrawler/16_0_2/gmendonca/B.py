import re

def recurssion(pancakes,flips, cut):
    if pancakes == len(pancakes) * pancakes[0] and pancakes[0] == '+':
        return flips
    else:
        str_cut = pancakes[0:cut]
        if str_cut[0] == '-':
            if str_cut[0] == str_cut[-1]:
                str_cut = str_cut.replace(str_cut[0], '+')
            else:
                str_cut = str_cut[0:cut-1].replace(str_cut[0], '+') + str_cut[-1:].replace(str_cut[-1:], '-')
        else:
            if str_cut[0] == str_cut[-1]:
                str_cut = str_cut.replace(str_cut[0], '-')
            else:
                str_cut = str_cut[0:cut-1].replace(str_cut[0], '-') + str_cut[-1:].replace(str_cut[-1:], '+')
        str_cut = str_cut[::-1]
        pancakes = str_cut + pancakes[cut:]
        flips += 1

        find_plus = re.search(r'[^+]', pancakes)
        find_minus = re.search(r'[^-]', pancakes)
        cut_plus = cut_minus = len(pancakes)
        if find_plus:
            cut_plus = find_plus.start()
        if find_minus:
            cut_minus = find_minus.start()
        cut = max(cut_plus,cut_minus)
        return recurssion(pancakes,flips, cut)


def double_recurence(pancakes):
    find_plus = re.search(r'[^+]', pancakes)
    find_minus = re.search(r'[^-]', pancakes)
    cut_plus = cut_minus = len(pancakes)
    if find_plus:
        cut_plus = find_plus.start()
    if find_minus:
        cut_minus = find_minus.start()
    cut = max(cut_plus,cut_minus)
    return min(recurssion(pancakes,0, cut),recurssion(pancakes,0, cut+1))


t = int(raw_input().strip())
for x in range(1,t+1):
    pancakes = raw_input().strip()
    print 'Case #%d: %d' %(x,double_recurence(pancakes))
