




T = int(input())


def count_inversions(pancakes):
    bottom = pancakes[::-1]
    current = '+'
    inversions = 0
    for pancake in bottom:
        if current != pancake:
            current = pancake
            inversions += 1
    return inversions


for t in range(T):
    stack = input()
    print('Case #{}: {}'.format(t+1, count_inversions(stack)))


    
        
