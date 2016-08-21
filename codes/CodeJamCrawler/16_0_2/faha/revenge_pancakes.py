"""
Google qualification round, Revenge of the Pancakes

@author: Faegheh Hasibi
"""

def revenge_pancakes(s):
    """Solves revenge of the pancakes problem"""
    count = 0
    while set(s) != {"+"}:
        decks = get_decks(s)
        # print(count, decks)
        count += 1
        decks[0] = flip(decks[0])
        s = "".join(decks)
    return count


def flip(s):
    """ Negates and reverses a string

    :param s: e.g, "--++-"
    :return: "+--++"
    """
    not_s = ""
    for char in s:
        not_s += "+" if char == "-" else "-"
    return not_s[::-1]


def get_decks(s):
    """Gets all decks with consequent similar signs

    :param s: sequence of signs; e.g. "--++-"
    :return: ["--", "++", "-"]
    """
    decks = []
    deck = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deck += s[i]
        else:
            decks.append(deck)
            deck = s[i]
    decks.append(deck)
    return decks


def main():
    # print(revenge_pancakes("-+-++-"))
    t = int(input())
    for i in range(1, t + 1):
        s = input().strip()
        print("Case #{}: {}".format(i, revenge_pancakes(s)))

if __name__ == "__main__":
    main()