# Code Jam 2016
# Raoul Veroy
import fileinput

stdin = fileinput.input()

def update_digits( digits = set([]),
                   num = None ):
    for x in str(num):
        digits.add(x)
    
results = {}
def get_sheep_number(start):
    global results
    if start == 0:
        return "INSOMNIA"
    if start in results:
        return results[start]
    digits = set([])
    num = start
    update_digits( digits, num )
    while len(digits) < 10:
        num += start
        update_digits( digits, num )
    results[start] = str(num)
    return results[start]

count = int(stdin.next())
for x in xrange(count):
    start = int(stdin.next().rstrip())
    shnum = get_sheep_number(start)
    print "Case #%d: %s" % (x+1, shnum)
