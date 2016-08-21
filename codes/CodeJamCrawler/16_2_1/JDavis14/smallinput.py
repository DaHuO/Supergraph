def remove(string, check):
    for c in check:
        string = string.replace(c, "", 1)
    return string


def check_if_in(string,check):
    copy = string
    for c in check:
        if c in copy:
            copy = copy.replace(c,"",1)
        else:
            return False
    return True


def remove_nums(string, number = ""):
    numbers = {"ZERO":0, "ONE":1, "TWO":2, "THREE":3, "FOUR":4, "FIVE":5, "SIX":6, "SEVEN":7, "EIGHT":8, "NINE":9}
    matches = [x for x in numbers if check_if_in(string,x)]
    if len(matches) == 0:
        if not string:
            return number
    else:
        for match in matches:
            if number:
                if int(number[-1]) <= numbers[match]:
                    for c in match:
                        string = string.replace(c, "", 1)
                    number += str(numbers[match])
                else:
                    return ""
            else:
                for c in match:
                    string = string.replace(c, "", 1)
                number += str(numbers[match])
            result = remove_nums(string, number)
            if result:
                return result
            else:
                number = number[:-1]
                string += match

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()

    #numbers = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

    val = remove_nums(s)

    print "Case #{}: {}".format(i, val)

