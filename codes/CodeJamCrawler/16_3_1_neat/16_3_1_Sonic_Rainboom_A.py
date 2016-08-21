import sys
import Queue


def solve(N, counts):
    counts.sort(reverse = True)
    answer = "" 
    while len(counts) > 0:
        if len(counts) >= 4:
            if counts[0][0] == counts[1][0] and counts[1][0] == counts[2][0] and counts[2][0] == counts [3][0]:
                counts[0][0] -= 1
                counts [1][0] -= 1
                answer += counts[0][1]
                answer += counts[1][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                    del counts[1]
                counts.sort(reverse = True)
            elif counts[0][0] == counts[1][0] and counts[1][0] == counts[2][0]:
                counts[0][0] -= 1
                answer += counts[0][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                counts.sort(reverse = True)
            elif counts[0][0] == counts[1][0]:
                counts[0][0] -= 1
                counts [1][0] -= 1
                answer += counts[0][1]
                answer += counts[1][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                    del counts[1]
            else:
                counts[0][0] -= 1
                answer += counts[0][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                
        elif len(counts) == 3:
            if counts[0][0] == counts[1][0] and counts[1][0] == counts[2][0]:
                counts[0][0] -= 1
                answer += counts[0][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                counts.sort(reverse = True)
            elif counts[0][0] == counts[1][0]:
                counts[0][0] -= 1
                counts[1][0] -= 1
                answer += counts[0][1]
                answer += counts[1][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                    del counts[0]
                counts.sort(reverse = True)
            else:
                counts[0][0] -= 1
                answer += counts[0][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                counts.sort(reverse = True)

        elif len(counts) == 2:
            if counts[0][0] == counts[1][0]:
                counts[0][0] -= 1
                counts[1][0] -= 1
                answer += counts[0][1]
                answer += counts[1][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                    del counts[0]
                counts.sort(reverse = True)
            else:
                counts[0][0] -= 1
                answer += counts[0][1]
                answer += " "
                if counts[0][0] == 0:
                    del counts[0]
                counts.sort(reverse = True)

        else:
            counts[0][0] -= 1
            answer += counts[0][1]
            answer += " "
            if counts[0][0] == 0:
                del counts[0]
            counts.sort(reverse = True)
                
    return answer

#in_file = open("input.txt", 'r')
in_file = open("A-small-attempt0.in", 'r')
#in_file = open("A-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()
    N = line[0]
    line = in_file.readline().strip().split()
    counts = []
    party = 65
    for elem in line:
        counts.append([int(elem), chr(party)])
        party += 1
    sol = solve(N, counts)
    print sol
    answer = "Case #" + str(case) + ": " + sol + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

