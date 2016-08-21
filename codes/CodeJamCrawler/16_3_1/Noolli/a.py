#
#
# def solve(number_of_parties,parties_count):
#     result = []
#     parties = {}
#     j = 0
#     for i in range(ord('A'), ord('A') + number_of_parties):
#         parties[chr(i)] = parties_count[j]
#         j+=1
#
#     sum_of_senatores = sum(parties_count)
#     while sum_of_senatores > 0:
#         orderes_parties = [(k, parties_count[k]) for k in parties.keys()]
#         orderes_parties.sort(key=lambda x: -x[1])
#
#         half = float(sum_of_senatores - 2) / 2
#         larger = [x for x in orderes_parties if x[1] > half]
#         if len(larger) == 1:
#             if larger[0][1] - 2 > 0:
#                 result.append(""+larger[0][0]+larger[0][0])
#                 parties[larger[0]] -= 2
#                 sum_of_senatores = sum(parties.values())
#                 continue
#             elif orderes_parties[1][1]>=1:
#                 result.append("" + larger[0][0] + orderes_parties[1][0])
#                 parties[larger[0]] -= 1
#                 parties[orderes_parties[1]] -= 1
#                 sum_of_senatores = sum(parties.values())
#                 continue
#             else:
#                 result.append("" + larger[0][0])
#                 parties[larger[0]] -= 1
#                 sum_of_senatores = sum(parties.values())
#                 continue
#         elif len(larger) == 2:
#             result.append("" + larger[0][0] + larger[1][0])
#             parties[larger[0]] -= 1
#             parties[larger[1]] -= 1
#             sum_of_senatores = sum(parties.values())
#             continue
#         elif len(larger) > 2:
#             other_half = float(sum_of_senatores - 1) / 2
#             other_larger = [x for x in orderes_parties if x[1] > other_half]
#             if len(other_larger) == 1:
#                 if other_larger[0][1] - 2 > 0:
#                     result.append("" + other_larger[0][0] + other_larger[0][0])
#                     parties[other_larger[0]] -= 2
#                     sum_of_senatores = sum(parties.values())
#                     continue
#                 elif orderes_parties[1][1] >= 1:
#                     result.append("" + other_larger[0][0] + orderes_parties[1][0])
#                     parties[other_larger[0]] -= 1
#                     parties[orderes_parties[1]] -= 1
#                     sum_of_senatores = sum(parties.values())
#                     continue
#                 else:
#                     result.append("" + other_larger[0][0])
#                     parties[other_larger[0]] -= 1
#                     sum_of_senatores = sum(parties.values())
#                     continue
#             elif len(other_larger) == 2:
#                 result.append("" + other_larger[0][0] + other_larger[1][0])
#                 parties[other_larger[0]] -= 1
#                 parties[other_larger[1]] -= 1
#                 sum_of_senatores = sum(parties.values())
#                 continue
#         else:
#



def solve2(number_of_parties,parties_count):
    result = []
    parties = {}
    j = 0
    for i in range(ord('A'), ord('A') + number_of_parties):
        parties[chr(i)] = parties_count[j]
        j+=1

    sum_of_senatores = sum(parties_count)
    while sum_of_senatores > 0:
        orderes_parties = [(k, parties[k]) for k in parties.keys()]
        orderes_parties.sort(key=lambda x: -x[1])
        ordered_numbers = [x[1] for x in orderes_parties]

        half = float(sum_of_senatores - 2) / 2

        if orderes_parties[0][1] >= 2:
            if max(ordered_numbers[1:]) > half:
                if orderes_parties[0][1] == orderes_parties[1][1]:
                    result.append(orderes_parties[0][0] + orderes_parties[1][0])
                    parties[orderes_parties[0][0]] -= 1
                    parties[orderes_parties[1][0]] -= 1
                else:
                    result.append(orderes_parties[0][0])
                    parties[orderes_parties[0][0]] -= 1

            else:
                result.append(orderes_parties[0][0]+orderes_parties[0][0])
                parties[orderes_parties[0][0]] -= 2
        else:
            if len(ordered_numbers) == 1:
                result.append(orderes_parties[0][0])
                parties[orderes_parties[0][0]] -= 1
            else:
                if len(ordered_numbers) == 3 and sum(ordered_numbers) == 3:
                    result.append(orderes_parties[0][0])
                    parties[orderes_parties[0][0]] -= 1
                else:
                    result.append(orderes_parties[0][0]+orderes_parties[1][0])
                    parties[orderes_parties[0][0]] -= 1
                    parties[orderes_parties[1][0]] -= 1

        sum_of_senatores = sum(parties.values())

    return " ".join(result)












def main():
    input_file = open('A-small-attempt2.in', 'r')
    output_file = open('A-small.out', 'w')
    number_of_cases = int(input_file.readline().strip())
    for i in range(1, number_of_cases + 1):
        number_of_parties = int(input_file.readline().strip())
        parties_count = [int(x) for x in input_file.readline().strip().split(" ")]
        result = solve2(number_of_parties,parties_count)
        print result
        output_file.write("Case #" + str(i) + ": " + result + "\n")

    input_file.close()

    # print solve2(3,[1,1,2])
if __name__ == "__main__":
    main()