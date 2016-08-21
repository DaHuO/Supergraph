file = open("in.in", "r")

def make_dict(list):
    dict = {}
    party = 'A'
    for el in list:
        dict[party] = el
        party = chr(ord(party) + 1)
    return dict

def rest(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum

def evacuate(parties):
    plan = []
    if not parties:
        return
    room = rest(parties)
    if room <= 2:
        plan.append(''.join(parties.keys()))
        return plan
    parties_s = sorted(parties.items(), key = lambda x: -x[1])
    party1 = parties_s[0]
    party2 = parties_s[1]
    if party1[1] == party2[1]:
        parties[party1[0]] -= 1
        if parties[party1[0]] == 0:
            del parties[party1[0]]
        parties[party2[0]] -= 1
        if parties[party2[0]] == 0:
            del parties[party2[0]]
        plan = evacuate(parties)
        plan.append(party1[0] + party2[0])
        return plan
    else:
        parties[party1[0]] -= 2
        if parties[party1[0]] == 0:
            del parties[party1[0]]
        plan = evacuate(parties)
        plan.append(party1[0] + party1[0])
        return plan

def out(list):
    res = ""
    for el in list:
        res += el + " "
    return res.rstrip()


cases = int(file.readline())

outfile = open("out.out", "w")

i = 1

for line in file:
    if len(line.split(" ")) > 1:
        senators = [int(x) for x in line.split(" ")]
        parties = make_dict(senators)
        plan = list(reversed(evacuate(parties)))
        if len(plan[len(plan) - 1] ) == 1:
            plan[len(plan) - 1] += plan[len(plan) - 2][1]
            plan[len(plan) - 2] = plan[len(plan) - 2][0]
        outfile.write("Case #" + str(i) + ": " + out(plan) + "\n")
        i += 1

outfile.close()
file.close()