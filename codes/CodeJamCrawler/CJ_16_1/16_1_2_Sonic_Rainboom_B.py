import sys

def find_list(N, lines):

    thing = {}
    for line in lines:
        for num in line:
            if num in thing:
                thing[num] = thing[num] + 1
            else:
                thing[num] = 1
    odds = []
    for key in thing.keys():
        if thing[key] % 2:
            odds.append(int(key))
    odds = sorted(odds)
    answer = ""
    for num in odds:
        answer += str(num) + " "
    return answer

    
        
    
in_file = open("B-large.in", 'r')
out_file = open("output.txt", 'w')

size = int(in_file.readline())

case = 1

while case <= size:
    N = int(in_file.readline())
    lines = []
    for i in range(0, 2*N - 1):
        lines.append(in_file.readline().strip().split())
    nums = find_list(N, lines)
    answer = "Case #" + str(case) + ": " + nums + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

