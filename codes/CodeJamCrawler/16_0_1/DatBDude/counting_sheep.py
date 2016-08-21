import sys

# Input
#
# The first line of the input gives the number of test cases, T.
# T test cases follow. Each consists of one line with a single integer N, the number Bleatrix has chosen.
#
# Output
#
# For each test case, output one line containing Case
# x: y, where x is the test case number (starting from 1) and y is the last number
# that Bleatrix will name before falling asleep, according to the rules described in the statement.


# takes an int and returns a list of unique ints in the number
def nums_visited(num):
    unique_nums =[]
    while(num > 0):
        unique_nums.append(num%10)
        num /= 10
    return set(unique_nums)


def is_complete(visited_set):
    if(visited_set == {0,1,2,3,4,5,6,7,8,9}):
        return True
    return False


def main(argv):

    f = open(argv, 'r')
    N = int(f.readline())

    for i in range(N):
        case = int(f.readline())
        visited = set()
        x = 1
        if( case == 0):
            print( "Case #%d: INSOMNIA" % (i+1))
        else:
            while( is_complete(visited) == False):
                visited = visited | nums_visited(x*case)
                x += 1
            print( "Case #%d: %d" % (i+1, (x-1)*case))

if __name__=="__main__":
    main(sys.argv[1])