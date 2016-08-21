def solve(n):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    for i in range(1, 101):
        product = str(i * n)
        for j in range(len(product)):           
            num = int(product[j])
            if num in numbers:
                numbers.remove(num)
                if (len(numbers) == 0):
                    return product        
    return "INSOMNIA"
        
    
if __name__ == "__main__":
    t = int(input()) 
    for i in range(1, t + 1):        
        n = int(input())              
        print("Case #{}: {}".format(i, solve(n)))
        
