def sheep_count(n):
    if n == 0:
        return 'INSOMNIA'
    numbers = set(['0','1','2','3','4','5','6','7','8','9'])
    counted_numbers = set([])
    count = 1
    m = 0
    while counted_numbers != numbers:
        m += n
        counted_numbers |= set(list(str(m)))
    return str(m)
        
def formatted_output(index, final_count):
    return 'Case #' + str(index) + ': ' + final_count


t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(raw_input())  # read a list of integers, 2 in this case
    print formatted_output(i, sheep_count(n))
    # check out .format's specification for more formatting options