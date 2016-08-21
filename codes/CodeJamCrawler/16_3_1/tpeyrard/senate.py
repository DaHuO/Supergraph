__author__ = 'tpeyrard'

from templates import *

test_input = readFrom()

nb_tests = int(test_input[0])
# nb_tests = 4

N = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']

print(test_input)
cpt = 0
for i in range(1, nb_tests * 2, 2):
    cpt+=1
    nb_parties = test_input[i]
    nb_senators = [int(senators) for senators in test_input[i + 1].split(' ')]
    print(i, " ---", str(nb_parties), " ", str(nb_senators))
    result = ""
    while sum(nb_senators) > 0:
        the_one = max(nb_senators)
        chosen = nb_senators.index(the_one)
        result += N[chosen]
        nb_senators[chosen] -= 1

        if max(nb_senators) == 1 and sum(nb_senators) == 2:
            result += ' '
        else:
            the_second = max(nb_senators)
            chosen = nb_senators.index(the_second)
            result += N[chosen] + ' '
            nb_senators[chosen] -= 1
    appendLineTo(aLine(cpt, result))




    # print(element)
    # appendLineTo(aLine(cpt, element))
    # cpt+=1

# writeTo(result)
