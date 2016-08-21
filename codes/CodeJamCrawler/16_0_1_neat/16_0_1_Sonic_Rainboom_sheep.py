import sys

def count_sheep(init):
    if init == 0:
        return -1
    count = 0
    nums_seen = {}
    sheep = init
    while(True):
        strnum = str(sheep)
        for char in strnum:
            if char in nums_seen:
                continue
            else:
                nums_seen[char] = 1
                count += 1
                if count == 10:
                    return sheep
        sheep += init
    
'''    
for num in range(0, 1000001):
    #sys.stdout.write(str(num))
    sheep = count_sheep(num)
    #sys.stdout.write("\t\t")
    #print sheep
print "Done"
'''

in_file = open("A-large.in", 'r')
out_file = open("output.txt", 'w')

size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline()
    sys.stdout.write(line.strip())
    num = int(line)
    sheep = count_sheep(num)
    sys.stdout.write("\t\t")
    print sheep
    if sheep == -1:
        answer = "Case #" + str(case) + ": INSOMNIA\n"
    else:
        answer = "Case #" + str(case) + ": " + str(sheep) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

