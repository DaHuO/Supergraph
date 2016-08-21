letters = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE"
numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

num_count = [dict() for i in range(10)]
for i, name in enumerate(numbers):
    for l in name:
        if l not in num_count[i]:
            num_count[i][l] = 0
        num_count[i][l] += 1


def recur(bank, num):
    if num == 10:
        for l in bank:
            if bank[l] > 0:
                return False
        return []
    me = num_count[num]
    how_many = 0
    available = True
    while available:
        result = recur(bank, num + 1)
        if result is not False:
            break
        for l in me:
            if me[l] > bank[l]:
                available = False
                break
        else:
            how_many += 1
            for l in me:
                bank[l] -= me[l]
    for _ in range(how_many):
        for l in me:
            bank[l] += me[l]

    if result is False:
        return False
    return [num] * how_many + result


t = int(input())
for case in range(1, t+1):
    bank = dict()
    for l in letters:
        bank[l] = 0
    line = input()
    for l in line:
        bank[l] += 1
    result = recur(bank, 0)
    print("Case #{}: {}".format(case, "".join(map(str, result))))
