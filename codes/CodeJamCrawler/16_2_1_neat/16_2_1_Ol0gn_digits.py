__author__ = 'sumant'

from collections import Counter


num_wc = {
    1: Counter('ONE'),
    2: Counter('TWO'),
    3: Counter('THREE'),
    4: Counter('FOUR'),
    5: Counter('FIVE'),
    6: Counter('SIX'),
    7: Counter('SEVEN'),
    8: Counter('EIGHT'),
    9: Counter('NINE'),
    0: Counter('ZERO')
}

glob_phone_num = ''
def get_phone_number(letters, prev_num, phone_num):
    # First try adding prev num
    curr_num = prev_num
    while len(letters) > 0:
        if curr_num > 9:
            return False
        num_found = True
        for c in num_wc[curr_num]:
            if not(c in letters and letters[c] >= num_wc[curr_num][c]):
                num_found = False
                break
        if not num_found:
            curr_num += 1
            continue

        next_letters = dict(letters)
        for c in num_wc[curr_num]:
            next_letters[c] -= num_wc[curr_num][c]
            if next_letters[c] == 0:
                next_letters.pop(c)
        if get_phone_number(next_letters, curr_num, phone_num + str(curr_num)):
            break
        else:
            curr_num += 1
    global glob_phone_num
    if glob_phone_num == '':
        glob_phone_num = phone_num
    return True

if __name__ == '__main__':
    # letters = Counter('OZONETOWERWEIGHFOXTOURISTOURNEONFOEETHER')
    # get_phone_number(letters, 0, '')
    # print glob_phone_num
    n = int(raw_input())
    for i in range(n):
        s = str(raw_input())
        letters = Counter(s)
        get_phone_number(letters, 0, '')
        print 'Case #%s: %s' % (i+1, glob_phone_num)
        glob_phone_num = ''

