__author__ = 'jaehoonlee88'


input_file = open('A-small-attempt1.in', "r")
output_file = open('output.txt', "w")

T = int(input_file.readline())


nums_word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def contain_num(arr, num):
    num_chs = list(nums_word[num])
    for ch in num_chs:
        if not arr.has_key(ch) or arr[ch] == 0:
            return False
        else :
            arr[ch] = arr[ch] - 1


    return True

def remove_num(arr, num):
    num_chs = list(nums_word[num])
    for ch in num_chs:
        arr[ch] = arr[ch] - 1
        if arr[ch] == 0:
            arr.pop(ch, None)

    return True


def find_num(arr, num):
    #print arr, num, len(arr.keys())

    if num == 10:
        return '', 0

    if len(arr.keys()) == 0:
        return '', 1

    if contain_num(arr.copy(), num):
        temp = arr.copy()
        remove_num(arr, num)
        result, correct = find_num(arr, num)
        if correct == 1:
            return str(num) + result, 1
        else:
            return find_num(temp, num+1)

    else :
        return find_num(arr, num+1)

for i in range(0, T):
    phone = input_file.readline().rstrip('\n')
    arr = {}
    for ch in list(phone):
        if arr.has_key(ch):
            arr[ch] = arr[ch] + 1
        else :
            arr[ch] = 1

    result, correct = find_num(arr, 0)
    output_file.write("Case #" + str(i+1) + ": " + result + '\n')


