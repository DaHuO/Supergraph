t = int(raw_input().strip())
for case in xrange(1, t + 1):
    k, c, s = map(int, raw_input().strip().split(' '))
    students = []
    for i in xrange(0, k, c):
        student = 0
        for j in xrange(c):
            student *= k
            if i + j < k: student += i + j
        students.append(student)
    result = None
    if len(students) > s:
        result = 'IMPOSSIBLE'
    else:
        result = ' '.join(map(lambda x: str(x + 1), students))
    print 'Case #%d: %s' % (case, result)
