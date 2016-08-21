def get_accurate_order(parties_members):
    result = []
    while(True):
        parties_members.sort(key = len, reverse = True)
        if len(parties_members[0]) == 0:
            break
        if(len(parties_members) != 3 or len(parties_members[0]) != 1):
            if len(parties_members[0]) == len(parties_members[1]):
                result.append(parties_members[0][0] + parties_members[1][0])
                parties_members[0] = parties_members[0][1:]
                parties_members[1] = parties_members[1][1:]
            else:
                result.append(parties_members[0][:2])
                parties_members[0] = parties_members[0][2:]
        else:
            result.append(parties_members[0])
            parties_members.remove(parties_members[0])

        for member in parties_members:
            if member == '':
                parties_members.remove(member)
        # print(result)
    return " ".join(result)

cases_number = int(input())
for case in range(1, cases_number + 1):
    parties_number = int(input())
    parties = []
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    for x in input().split():
        parties.append(int(x) * letters[index])
        index += 1
    answer = get_accurate_order(parties)
    print("Case #" + str(case) + ":", answer)