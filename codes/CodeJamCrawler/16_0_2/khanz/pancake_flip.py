def pancake_flip(state):
    count = 0
    curr = '+'
    for i in range(len(state)-1, -1, -1):
        if state[i] != curr:
            curr = state[i]
            count += 1
    return count

def main():
    n = int(input())
    inputs = []
    for i in range(n):
        inputs.append(input())
    for i in range(n):
        print('Case #{}: {}'.format(i+1, pancake_flip(inputs[i])))
        
if __name__ == "__main__":
    main()
