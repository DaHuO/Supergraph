def solve(pancakes, current_index, target):
    other = (target + 1) % 2
    move_count = 0
    
    while current_index >= 0 and pancakes[current_index] == target:
        current_index -= 1

    if current_index == -1:
	return 0	

    while current_index >= 0 and pancakes[current_index] == other:
        current_index -= 1

    if current_index == -1:
	return 1
    
    return solve(pancakes, current_index, other) + 1

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        pancakes = raw_input()
	pancakes = [1 if a == '-' else 0 for a in pancakes]
        result = solve(pancakes, len(pancakes) - 1, 0)
        print 'Case #%d: %s' % (i, result)

if __name__ == '__main__':
    main()
