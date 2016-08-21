import sys

def main(data):
    answer = []
    for char in data:
        if not answer or answer[0] <= char:
            answer = [char] + answer
        else:
            answer.append(char)

    return "".join(answer)

T = int(raw_input())
for x in xrange(T):
    print "Case #" + str(x + 1) + ": " + main(raw_input())
