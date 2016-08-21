import heapq
T = int(raw_input())

parties_name = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for case in range(1, T+1):
    N = int(raw_input())
    senators = map(int, raw_input().strip().split())
    sol = ""
    total_number = sum(senators)
    while total_number > 0:
        max_senators = heapq.nlargest(3,  enumerate(senators), key=lambda x: x[1])
        take = 2
        the_same = True
        half_2 = float(total_number - 2) / 2
        if len(max_senators) > 2 and max_senators[2][1] > half_2:
            take = 1
        if max_senators[1][1] > half_2:
            the_same = False

        sol += str(parties_name[max_senators[0][0]])
        senators[max_senators[0][0]] -= 1
        total_number -= take
        if take == 2:
            if the_same:
                sol += str(parties_name[max_senators[0][0]])
                senators[max_senators[0][0]] -= 1
            else:
                sol += str(parties_name[max_senators[1][0]])
                senators[max_senators[1][0]] -= 1
        sol += " "



    print "Case #{}: {}".format(case, sol)
