
import heapq
import string

test_case = int(input())

for case_no in range(test_case):
    result = ['Case #' + str(case_no + 1) + ':']
    party = [(-int(people_num), party_name)
             for party_name, people_num in zip(list(string.ascii_uppercase)[:int(input())], input().split(' '))]
    heapq.heapify(party)
    while True:
        if len(party) <= 0:
            print(' '.join(result))
            break
        if len(party) == 2:
            first = heapq.heappop(party)
            second = heapq.heappop(party)
            if first[0] < second[0]:
                result.append(first[1])
                if first[0] < -1:
                    heapq.heappush(party, (first[0] + 1, first[1]))
                heapq.heappush(party, second)
                continue
            if first[0] > second[0]:
                result.append(second[1])
                heapq.heappush(party, first)
                if second[0] < -1:
                    heapq.heappush(party, (second[0] + 1, second[1]))
                continue
            result.append(first[1] + second[1])
            if first[0] < -1:
                heapq.heappush(party, (first[0] + 1, first[1]))
            if second[0] < -1:
                heapq.heappush(party, (second[0] + 1, second[1]))
            continue
        if len(party) == 3:
            first = heapq.heappop(party)
            second = heapq.heappop(party)
            if first[0] == second[0]:
                result.append(first[1])
                if first[0] < -1:
                    heapq.heappush(party, (first[0] + 1, first[1]))
                heapq.heappush(party, second)
                continue
            result.append(first[1] + second[1])
            if first[0] < -1:
                heapq.heappush(party, (first[0] + 1, first[1]))
            if second[0] < -1:
                heapq.heappush(party, (second[0] + 1, second[1]))
            continue
        first = heapq.heappop(party)
        if first[0] < -1:
            heapq.heappush(party, (first[0] + 1, first[1]))
        second = (-1, '') if len(party) <= 0 else heapq.heappop(party)
        result.append(first[1] + second[1])
        if second[0] < -1:
            heapq.heappush(party, (second[0] + 1, second[1]))
