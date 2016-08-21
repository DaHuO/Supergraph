array = []
with open('input_small.txt','r') as reader :
    for line in reader :
        array.append(int(line))


for case in range(0,array[0]):

    N = array[case+1]
    index = 1

    if N == 0:
        print "Case #" + str(case+1) + ": INSOMNIA"
    else:
        numbers = [0,1,2,3,4,5,6,7,8,9]

        while len(numbers) > 0:
            tmp = N*index
            list_of_ints = [int(i) for i in str(tmp)]
            numbers = [x for x in numbers if x not in list_of_ints]
            index += 1
        print "Case #" + str(case) + ": " + str(tmp)


