def maneuver(data):

    neg_in = indexes(data, "-")
    count = 0

    if len(neg_in) == len(data):
        count += 1
        return count
    else:
        while len(data) > 1:
            pos_in = indexes(data, "+")
            if len(pos_in) != len(data):
                count += 1
                if data[len(data)-1] == '+':
                    p = poslen(data)
                    data = flip(data[:len(data)-p])
                else:
                    data = flip(data)
            else:
                return count

        return count


def poslen(data):
    pos_count = 0
    count = 0

    while count < len(data):
        if data[len(data)-1] == "+":
            pos_count += 1
            data = data[:len(data)-1]
        else:
            break

    return pos_count


def indexes(data_, value):
    return [i for i, val in enumerate(data_) if val == value]


def flip(faces):

    p = "+"
    n = "-"

    pos_index = indexes(faces, "+")

    if len(pos_index) != len(faces):
        for i, j in enumerate(faces):
            if j == p:
                faces[i] = n
            else:
                faces[i] = p
        return faces

with open("B-large.in") as data, open("output.in", "w") as data1:

    test_cases = data.readline()
    final_count = 0

    for i in data:
        final_count += 1
        data = list(i.strip("\n"))
        ans = maneuver(data)
        # print("Case #{}: {}" .format(final_count, ans))
        data1.write("Case #{}: {}\n" .format(final_count, ans))
