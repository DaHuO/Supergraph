seen = []
counter = 0
seen_1 = False
seen_2 = False
seen_3 = False
seen_4 = False
seen_5 = False
seen_6 = False
seen_7 = False
seen_8 = False
seen_9 = False
seen_0 = False
def break_numbers(n):
    str_n = str(n)
    looper = 0
    numbers_array = []
    for i in range(0,len(str_n)):
        numbers_array.append(str_n[looper])
        looper += 1
    return numbers_array

def keeping_track(numbers_array):
    global seen
    for numbers in numbers_array:
        seen.append(numbers)
        
def checking_seen(seen):
    global counter
    global seen_1
    global seen_2
    global seen_3
    global seen_4
    global seen_5
    global seen_6
    global seen_7
    global seen_8
    global seen_9
    global seen_0
    seen_numbers = [1,2,3,4,5,6,7,8,9,0]
    for items in seen:
        for numbers in seen_numbers:
            if int(items) == int(numbers):
                if int(items) == 1:
                    seen_1 = True
                if int(items) == 2:
                    seen_2 = True
                if int(items) == 3:
                    seen_3 = True
                if int(items) == 4:
                    seen_4 = True
                if int(items) == 5:
                    seen_5 = True
                if int(items) == 6:
                    seen_6 = True
                if int(items) == 7:
                    seen_7 = True
                if int(items) == 8:
                    seen_8 = True
                if int(items) == 9:
                    seen_9 = True
                if int(items) == 0:
                    seen_0 = True
                
    if seen_1 and seen_2 and seen_3 and seen_4 and seen_5 and seen_6 and seen_7 and seen_8 and seen_9 and seen_0:
        return True

def main(n):
    global seen
    global counter
    multiplier = 1
    run = True
    while run:
        n_number = n * multiplier
        broken = break_numbers(n_number)
        keeping_track(broken)
        check = checking_seen(seen)
        if check:
            run = False
            return n_number
        if multiplier > 10 and n == 0:
            return "INSOMNIA"
        else:
            multiplier += 1

file = open("A-large.in","rt")
case = 1
line_on_file = 1
for lines in file:
    if line_on_file > 1:
        mult = main(int(lines))
        file = open("output.txt","at")
        file.write("Case #"+str(case) + ": "+str(mult)+"\n")
        file.close()
        print ("Case #"+str(case) + ": "+str(mult))
        case += 1
        del seen[:]
        seen_1 = False
        seen_2 = False
        seen_3 = False
        seen_4 = False
        seen_5 = False
        seen_6 = False
        seen_7 = False
        seen_8 = False
        seen_9 = False
        seen_0 = False
    line_on_file += 1
    
        
    
        
        
