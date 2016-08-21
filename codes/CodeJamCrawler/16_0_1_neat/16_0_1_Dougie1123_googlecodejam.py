f = open('input.txt')
lines = f.readlines()
f.close()

output = open('output.txt','w')
for i in range(int(lines[0])):
    set_nums = set()
    n = int(lines[i+1])
    next = n
    if n == 0:
        output.write("Case #" + str(i + 1) + ": " + 'INSOMNIA' + "\n")
    else:
        ctr = 1
        while len(set_nums) != 10:
            #add the number
            for num in str(next):
                set_nums.add(num)
            if len(set_nums) == 10:
                break
            ctr += 1
            next = n*ctr


        output.write("Case #" + str(i+1) + ": " + str(next) + "\n")
output.close()