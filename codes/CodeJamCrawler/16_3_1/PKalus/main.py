
def count_all(lst):
    count = 0
    for item in lst:
        count += item
    return count


def check_majority(senator, count):
    half = count/2
    if count % 2 == 1:
        half += 0.5
    for sen in senator:
        if sen > half:
            return False
    return True


def find_max(lst):
    return lst.index(max(lst))


def count_max(lst):
    return lst.count(max(lst))


def magic(senator):
    evac = ""
    count = count_all(senator)
    while max(senator) != 0:
        i_max = find_max(senator)
        evac += chr(i_max+65)
        senator[i_max] -= 1
        # print(senator)
        # print(check_majority(senator, count))
        i_max = find_max(senator)
        if senator[i_max] != 0:
            if max(senator) != 1 or (max(senator) == 1 and count_max(senator) == 1):
                evac += chr(i_max + 65) + " "
                senator[i_max] -= 1
                # print(senator)
                # print(check_majority(senator, count))
            else:
                evac += " "
    return evac

file = open("input.in", 'r')
test = file.readline()

output = open("output.out", 'w')


for i in range(int(test)):
    file.readline()
    line = file.readline()
    senators = [int(s) for s in line.split() if s.isdigit()]
    output.write("Case #" + str(i + 1) + ": " + magic(senators) + "\n")
    output.flush()
    # print(senators)
    # print(magic(senators))
