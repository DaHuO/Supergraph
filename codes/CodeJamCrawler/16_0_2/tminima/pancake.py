
def rev(order):
    order = order.replace("+", "0")
    order = order.replace("-", "+")
    order = order.replace("0", "-")
    return order


def make_new_order(order, ele):
    pos = order.find(ele)
    order = rev(order[:pos]) + order[pos:]
    return order


def calc_flips(order):
    order_len = len(order)
    flips = 0
    while order.count("+") != order_len:
        hap = order.count("+")
        non_hap = order.count("-")
        # print(hap, non_hap)
        if non_hap == order_len:
            order = rev(order)
        # elif hap == non_hap:
        #     if order[0] == "+":
        #         order = make_new_order(order, "-")
        #     else:
        #         order = make_new_order(order, "+")
        # elif hap >= non_hap:
        #     if order[0] == "+":
        #         order = make_new_order(order, "-")
        #     else:
        #         order = make_new_order(order, "+")
        else:
            if order[0] == "+":
                order = make_new_order(order, "-")
            else:
                order = make_new_order(order, "+")
        # order = new_order
        # print(order, end=" ")
        flips += 1

    return flips


def get_flips(data):
    t = int(data[0])
    for i in range(t):
        order = data[i + 1]
        flips = 0
        if order.count("+") == len(order):
            flips = 0
        elif order.count("-") == len(order):
            flips = 1
        else:
            flips = calc_flips(order)

        # print(order)
        # print("\n{} Case #{}: {}".format(order, i + 1, flips))
        print("Case #{}: {}".format(i + 1, flips))


if __name__ == "__main__":
    # data = open("input.txt", "r").readlines()
    data = open("B-large.in", "r").readlines()
    data = [i.strip() for i in data]

    get_flips(data)
