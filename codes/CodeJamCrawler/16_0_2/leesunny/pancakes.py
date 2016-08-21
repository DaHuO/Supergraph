def main():
    i = 0
    while True:
        try:
            t = input()
            if i != 0:  # Skip first line
                print("Case #{}: {}".format(i, pancakes(t)))
        except EOFError:
            break
        i += 1


def parse_pancakes(s):
    return [True if x == "+" else False for x in list(s.rstrip())]


def all_are_in_orientation(pans, orientation):
    for p in pans:
        if not p == orientation:
            return False

    return True


def pancakes(p):
    pans = parse_pancakes(p)
    return count_flips(pans)


def count_flips(pans, orientation=True):
    """
    Calculate the number of flips to change all pans to the given orientation

    Note: Similar to hanoi problem, we recursively change the first part of
        -+-++ to ---++ and then add one flip to +++++
    """
    if all_are_in_orientation(pans, orientation):
        return 0
    else:
        last_wrong_pancake = index_of_last(not orientation, pans)
        return count_flips(pans[0:last_wrong_pancake + 1], not orientation) + 1


def index_of_last(item, pans):
    return len(pans) - pans[::-1].index(item) - 1


def flip(pans):
    return [True if not x else False for x in reversed(pans)]


if __name__ == "__main__":
    main()
