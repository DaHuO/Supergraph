def check_equal(lst):
    return not lst or lst.count(lst[0]) == len(lst)

def invert(s):
    if s == '+':
        return '-'
    else:
        return '+'

def invert_list(a_list, num):
    new_list = ''
    i = num
    while i > 0:
        new_list = new_list + invert(a_list[i-1])
        i -= 1
    if num < len(a_list):
        new_list = new_list + a_list[num:]
    return new_list

def delete_end_if_positive(str):
    if str[-1] == '+':
        delete_size = len(str.split('-')[-1])
        delete_size = 0 - delete_size
        str = str[:delete_size]
    return str

line = raw_input()
T = int(line)
pancakes = []

for e in range(0, T):
    line = raw_input()
    pancakes.append(line)
    
case = 0
for elem in pancakes:
    case +=1
    i = 0
    all_happy = False
    while not all_happy:
        if check_equal(elem) and elem[0] == '+':
            all_happy = True
        else:
            elem = delete_end_if_positive(elem)
            if elem.index('-') == 0:
                elem = invert_list(elem, len(elem))
            else:
                elem = invert_list(elem, elem.index('-'))
            i += 1
    print "Case #" + str(case) + ": " + str(i)