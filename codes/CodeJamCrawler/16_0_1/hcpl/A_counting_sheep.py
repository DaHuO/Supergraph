def split_digits(num):
    digits = []
    
    while num:
        digits.append(num % 10)
        num //= 10
    
    return digits

def count_last_num(init_num):
    if init_num == 0:
        return 'INSOMNIA'
    else:
        visited = {i: False for i in range(10)}
        num = init_num
        
        while True:
            for d in split_digits(num):
                visited[d] = True
            
            if all(visited.values()):
                break
            
            num += init_num
        
        return num


def main():
    count = int(input())
    
    for i in range(count):
        current = int(input())
        print('Case #%d: %s' % (i + 1, count_last_num(current)))

if __name__ == '__main__':
    main()