
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
instances = []
for i in xrange(1, t + 1):
    instances.append(int(raw_input()))


#t,instances = read_problem
for i in range(len(instances)):
    if not (instances[i]):
        print "CASE #" + str(i+1) + ':' +  " INSOMNIA"
        continue
    base = instances[i]
    seen = set(str(base))
    iteration = 1
    while len(seen) < 10:
        new_number = base * iteration
        seen = seen.union(set(str(new_number)))
        iteration +=1
    print "CASE #" + str(i+1) + ': ' + str(new_number)







