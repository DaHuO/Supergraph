DIGIT_STRS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
STR_TO_NUM = {
        "ZERO": 0,
        "ONE": 1,
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5,
        "SIX": 6,
        "SEVEN":7,
        "EIGHT": 8,
        "NINE": 9
}

def sort_by_length(digit_strs):
    result = map(lambda x: (x, len(x)), digit_strs)
    result = [x[0] for x in sorted(result, key=lambda x : x[1])]
    return result

def str_to_dict(string):
    result = {}
    for s in string:
        if s not in result:
            result[s] = 0
        result[s] += 1
    return result


def helper(slen, sdict, result, digit_list):
    #print "HELPER slen={} result={}".format(slen, result)
    for digit in digit_list:
        remain = slen - len(digit)
        if remain != 0 and remain < 3:
            continue

        found = True
        sdict_copy = sdict.copy()
        for d in digit:
            if d in sdict_copy and sdict_copy[d] > 0:
                sdict_copy[d] -= 1
            else:
                found = False
                break

        if found: 
            result.append(STR_TO_NUM[digit])
            if remain == 0 or helper(remain, sdict_copy, result, digit_list):
                return True
            result.pop()

    return False

def get_number(string, digit_list):
    sdict = str_to_dict(string)
    result = []
    helper(len(string), sdict, result, digit_list)
    return "".join([str(d) for d in sorted(result)])


if __name__ == "__main__":
    digit_list = sort_by_length(DIGIT_STRS)
    T = int(raw_input())
    for i in range(T):
        string = raw_input()
        print "Case #{}: {}".format(i + 1, get_number(string, digit_list))




