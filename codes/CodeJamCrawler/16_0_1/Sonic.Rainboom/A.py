import sys

in_file = open("A-large.in", 'r')
out_file = open("output.txt", 'w')


def find_word(string):
    answer = ""
    for char in string:
        if answer == "":
            answer += char
        elif ord(char) >= ord(answer[0]):
            answer = char + answer
        else:
            answer += char
    return answer
            
    

    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip()
    word = find_word(line)

    answer = "Case #" + str(case) + ": " + word + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

