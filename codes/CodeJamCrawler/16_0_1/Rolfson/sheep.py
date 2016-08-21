f = open('small.in')
out = open('small.out', 'w')
num_cases = int(f.readline())
for x in range(num_cases):
    counter = 1
    nums = [0,1,2,3,4,5,6,7,8,9]
    original = int(f.readline())
    new = original
    while nums != []:
        new = original*counter
        counter = counter+1
        for char in str(new):
            for num in nums:
                if num == int(char):
                    nums.remove(num)
                    #print num, "removed"
        if counter > 1000000:
            answer = "INSOMNIA"
            nums = []
    if counter < 1000000:
        answer = str(new)
    out.write("Case #" + `x+1` + ":" + " " + answer + "\n")
