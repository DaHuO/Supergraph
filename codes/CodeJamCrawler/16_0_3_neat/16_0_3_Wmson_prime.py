def gen_primes():
    Prime_dict = {}
    # The running integer that's checked for primeness
    q = 2
    while True:
        if q not in Prime_dict:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            Prime_dict[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in Prime_dict[q]:
                Prime_dict.setdefault(p + q, []).append(p)
            del Prime_dict[q]

        q += 1



def is_jamcoin(number):
    base_2 = 0
    base_3 = 0
    base_4 = 0
    base_5 = 0
    base_6 = 0
    base_7 = 0
    base_8 = 0
    base_9 = 0
    base_10 = 0
    cur_pow = 0
    ret_str = ''
    for num in reversed(number):
        base_2 += num * 2 **cur_pow
        base_3 += num * 3 **cur_pow
        base_4 += num * 4 **cur_pow
        base_5 += num * 5 **cur_pow
        base_6 += num * 6 **cur_pow
        base_7 += num * 7 **cur_pow
        base_8 += num * 8 **cur_pow
        base_9 += num * 9 **cur_pow
        base_10 += num * 10 **cur_pow
        cur_pow += 1
    div_2 = get_divisor(base_2)
    if div_2 == -1:
        return ''
    div_3 = get_divisor(base_3)
    if div_3 == -1:
        return ''
    div_4 = get_divisor(base_4)
    if div_4 == -1:
        return ''
    div_5 = get_divisor(base_5)
    if div_5 == -1:
        return ''
    div_6 = get_divisor(base_6)
    if div_6 == -1:
        return ''
    div_7 = get_divisor(base_7)
    if div_7 == -1:
        return ''
    div_8 = get_divisor(base_8)
    if div_8 == -1:
        return ''
    div_9 = get_divisor(base_9)
    if div_9 == -1:
        return ''
    div_10 = get_divisor(base_10)
    if div_10 == -1:
        return ''
    return str(div_2) + ' ' + str(div_3) + ' ' + str(div_4) + ' ' + str(div_5) + ' ' + str(div_6) + ' ' + str(div_7) + ' ' +  str(div_8) + ' ' + str(div_9) + ' ' + str(div_10)




def get_divisor(num):
    if num % 2 == 0:
        return 2
    cur_div = 3
    while True:
        if cur_div* cur_div > num:
            break
        if num % cur_div == 0:
            return cur_div
        cur_div += 2
    return -1

raw_input()
line = raw_input().split()
num_dig = int(line[0])
num_gen = int(line[1])

cur_num = [1] +[0] * (num_dig - 2) + [1]

def next_num():
    num_needed = num_dig - 2
    if cur_num[num_needed + 1] == 0:
        cur_num[num_needed + 1] = 1
    else :
      cur_num[num_needed] = 0
      for i in range(1, num_needed):
          if cur_num[num_needed - i] == 0:
              cur_num[num_needed - i] = 1
              return
          cur_num[num_needed - i] = 0

cur_amount = 0
print("Case #1:")
while True:
    if cur_amount == num_gen:
        break
    ret = is_jamcoin(cur_num)
    if ret != '':
        print (''.join(str(e) for e in cur_num) + ' ' + ret)
        cur_amount += 1
    next_num()
