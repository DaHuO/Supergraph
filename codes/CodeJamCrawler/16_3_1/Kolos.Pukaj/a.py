import string
import operator

t = int(raw_input())
alphabet = list(string.ascii_uppercase)

for i in range(t):
        parties = int(raw_input())
        senators = map(int, raw_input().split())
        senate = {alphabet[j]: senators[j] for j in range(parties)}
        lst = []
        sorted_x = sorted(senate.items(), key=operator.itemgetter(1), reverse=True)
        if parties == 2:
                while sorted_x[0][1] != sorted_x[1][1]:
                        lst.append(sorted_x[0][0])
                        senate[sorted_x[0][0]] -= 1
                        sorted_x = sorted(senate.items(), key=operator.itemgetter(1), reverse=True)
                for x in range(sorted_x[0][1]):
                      lst.append(sorted_x[0][0]+sorted_x[1][0])
                str_to_print = lst[0]
                for x in lst[1:]:
                        str_to_print += ' '+x
                print "Case #{}: {}".format(i+1, str_to_print)
        else:
                while sorted_x[0][1] != 1 or sorted_x[1][1] != 1 or sorted_x[2][1] != 0:
                        lst.append(sorted_x[0][0])
                        senate[sorted_x[0][0]] -= 1
                        sorted_x = sorted(senate.items(), key=operator.itemgetter(1), reverse=True)
                lst.append(sorted_x[0][0]+sorted_x[1][0])
                str_to_print = lst[0]
                for x in lst[1:]:
                        str_to_print += ' '+x
                print "Case #{}: {}".format(i+1, str_to_print)