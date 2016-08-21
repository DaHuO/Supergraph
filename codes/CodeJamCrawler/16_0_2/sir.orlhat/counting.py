myfile = open('B-large.in' , 'r')
answer = open('B-large.out','w')

T = myfile.readline()
T = int(T)
T_count = 1

while ( T != 0):
    pancakes = myfile.readline()
    pancake = pancakes.strip()

    no_of_flips = len(pancake)

    counter = 0
    result = 0

    if pancake[no_of_flips-1] == '-':
        result +=1

    while ( counter < (no_of_flips-1)):
        counter+=1

        if (pancake[(counter-1)] != pancake[counter]):
            result+=1
    print("Case #" + str(T_count) + ': ' + str(result), file = answer)

    T_count +=1

    T-=1
answer.close()
