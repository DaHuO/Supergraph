
def make_bag(string):
    bag_of_letters = {}
    for c in string:
        if c in bag_of_letters:
            bag_of_letters[c] += 1
        else:
            bag_of_letters[c] = 1
    return bag_of_letters

_numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

NUMBERS = [make_bag(n) for n in _numbers]

def remove_numbers(letter, number, phone_dict):
    result = 0
    while letter in phone_dict:
        for key in number:
            if key not in phone_dict:
                return result, phone_dict

        for key in number:
            phone_dict[key] -= 1
            if phone_dict[key] == 0:
                phone_dict.pop(key, None)

        result += 1

    return result, phone_dict


def solve(a):
    phone_dict  = make_bag(a)
    # EIGHT
    nums = {i:0 for i in range(10)}

    nums[8], phone_dict =  remove_numbers("G", NUMBERS[8], phone_dict)
    nums[6], phone_dict =  remove_numbers("X", NUMBERS[6], phone_dict)
    nums[0], phone_dict =  remove_numbers("Z", NUMBERS[0], phone_dict)
    nums[2], phone_dict =  remove_numbers("W", NUMBERS[2], phone_dict)
    nums[4], phone_dict =  remove_numbers("R", NUMBERS[4], phone_dict)
    nums[3], phone_dict =  remove_numbers("H", NUMBERS[3], phone_dict)
    nums[5], phone_dict =  remove_numbers("F", NUMBERS[5], phone_dict)
    nums[7], phone_dict =  remove_numbers("V", NUMBERS[7], phone_dict)
    nums[1], phone_dict =  remove_numbers("O", NUMBERS[1], phone_dict)
    nums[9], phone_dict =  remove_numbers("I", NUMBERS[9], phone_dict)

    res = [str(k)*nums[k] for k in sorted(nums)]
    return "".join(res)


f = open("input.txt", "r+")
lines = tuple(f)

with open("output.txt", "w+") as o:
    for i in range(1, len(lines)):
        o.write("Case #%d: %s\n" % (i, solve(lines[i].strip())))
