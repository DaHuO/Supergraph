
def flip_pancakes(pancake_pile, i_elem):
    #print("Fliping pile from pos:0 to pos: " + str(i_elem) + " for list: " + str(pancake_pile))

    pancake_pile[0:i_elem] = pancake_pile[0:i_elem][::-1]
    for idx,elem in enumerate(pancake_pile[0:i_elem]):
        #print ("elem: " + elem)
        if elem == '-':
            pancake_pile[idx] = '+'
        else:
            pancake_pile[idx] = '-'

    #print("Final flipped pile: " + str(pancake_pile))
    return pancake_pile

def count_maneuver(pancake_pile):
    #print ("counting sheeps for: %s" % n)

    num_maneuver = 0

    while '-' in pancake_pile:
        #print("First elem of pancake_pile: ")
        if pancake_pile[0] == '-':
            try:
                idx = pancake_pile.index('+')
                num_maneuver += 1
                pancake_pile = flip_pancakes(pancake_pile, idx)

            except ValueError:
                num_maneuver += 1
                pancake_pile = flip_pancakes(pancake_pile, len(pancake_pile))
        else:
            idx = pancake_pile.index('-')
            pancake_pile = flip_pancakes(pancake_pile, idx)
            num_maneuver += 1

    return num_maneuver


if __name__ == "__main__":
    x = int(input())

    for i in range(1,x+1):
        s = input()
        pancake_pile = list(s)
        #print ("initial pancake_pile: " + str(pancake_pile))

        num_maneuver = count_maneuver(pancake_pile)
        #print("$%$%FINAL pancake_pile: " + str(pancake_pile))

        print("Case #{}: {}".format(i, num_maneuver))