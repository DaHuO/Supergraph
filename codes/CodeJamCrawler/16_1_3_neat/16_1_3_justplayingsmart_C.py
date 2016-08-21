##input = open('C-sample-input.txt', 'r')
##output = open('C-sample-output.txt', 'w')

input = open('C-small-attempt1.in', 'r')
output = open('C-small.out', 'w')

##input = open('C-large.in', 'r')
##output = open('C-large.out', 'w')

from itertools import permutations as perms

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(n, f):
    answer = False
    nums = n
    friends = {}
    for person in range(len(f)):
        friends[person+1] = f[person]
    print friends
    while not answer:
        print nums
        for perm in perms(range(1, n+1), nums):
##            print perm
            success = True
            for i in range(nums):
##                print i+1
                if i == 0:
                    if friends[perm[i]] == perm[1] or friends[perm[i]] == perm[-1]:
                        continue
                    else:
##                        print 'failure'
                        success = False
                        break
                elif i == nums - 1:
                    if friends[perm[i]] == perm[-2] or friends[perm[i]] == perm[0]:
                        continue
                    else:
##                        print 'failure'
                        success = False
                        break
                else:
                    if friends[perm[i]] == perm[i-1] or friends[perm[i]] == perm[i+1]:
                        continue
                    else:
##                        print 'failure'
                        success = False
                        break
            if success:
                print perm
                return nums
        nums -= 1
    return

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        n = read_int()
        f = read_ints()
##        if case == 4:
        solution = solve(n, f)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        




main()
input.close()
output.close()
    
