#!/usr/bin/env python

ALPHABET = 'ABCDEFGHIJKLMNOPQSRTUVWXYZ'

def merge_list(sub_list1, sub_list2):
    merged_list = []
    sub_list1.sort(reverse=True)
    i = 0
    for n, p in sub_list1:
        found = False
        while (i < len(sub_list2)):
            if sub_list2[i][0] > n:
                merged_list.append((sub_list2[i]))
                i += 1
            else:
                merged_list.append((n,p))
                found = True
                break
        if not found:
            merged_list.append((n,p))

    for j in range(i,len(sub_list2)):
        merged_list.append((sub_list2[i]))
    return merged_list


def next_step(no_senators):
    if len(no_senators) <1 :
        return None

    result = ''
    if len(no_senators) == 1:
        n, p = no_senators[0]
        if n >= 2:
            n -= 2
            result += p+p
        else:
            n -= 1
            result += p
        new_list = [(n,p)] if n > 0 else []
        return (result, new_list)

    n1, p1 = no_senators[0]
    n2, p2 = no_senators[1]


    if n1 == n2:
        if n1 > 1 or len(no_senators) > 3 or len(no_senators) == 2:
            n1 -= 1
            n2 -= 1
            result += p1 + p2
        else:
            n1 -= 1
            result += p1
    elif len(no_senators) > 2:
        n1 -= 2
        result += p1+p1
    else:
        n1 -= 1
        result += p1

    sub_list2 = no_senators[2:]
    sub_list1 = []
    if n1 > 0:
        sub_list1.append((n1, p1))
    if n2 > 0:
        sub_list1.append((n2, p2))
    new_list = merge_list(sub_list1, sub_list2)
    return (result, new_list)





if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            if line_index % 2 == 0:
                no_parties = int(line.strip())
            else:
                no_senators = zip([int(v) for v in line.strip().split()],ALPHABET)
                no_senators.sort(reverse=True)


                text_result = None
                while True:
                    result = next_step(no_senators)
                    if result is None:
                        break

                    s, no_senators = result
                    if text_result is None:
                        text_result = s
                    else:
                        text_result += ' ' + s

                print "Case #%d: %s" % (line_index/2+1, text_result)


            line_index += 1

