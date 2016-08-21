def countingSheep(n):
    if n == 0:
        return "INSOMNIA"

    # This set indicates if a digit is named
    d = set()
    count = 10
    
    # len(cur)>= len(store)
    cur = [int(x) for x in str(n)]
    store = [int(x) for x in str(n)]
    n = len(str(n))
    
    for x in store:
        if x not in d:
            d.add(x)
            count -= 1

    # When count = 0, all digits are named.
    while count>0:
        carry = 0
            
        # Add current by score
        for i in range(1,n+1):
            val = cur[-i] + store[-i] + carry
            cur[-i] = val % 10
            carry = val // 10
            
        # Handle the extra characters in cur
        if len(cur)>n:
            for i in range(len(cur)-n-1,-1,-1):
                val = cur[i] + carry
                cur[i] = val % 10
                carry = val // 10
                
        # Increment the size of cur if at the end carry=1
        if carry == 1:
            cur = [1] + cur
        
        for x in cur:
            if x not in d:
                d.add(x)
                count -= 1

    # Return the integer in the form of a string
    return ''.join(str(e) for e in cur)

# main function
if __name__ == "__main__":
    T = int(input())
    nums = [0 for i in range(T)]
    res = [0 for i in range(T)]

    # Take input
    for i in range(T):
        nums[i] = int(input())

    for i in range(T):
        print("Case #%d: " %(i+1) + countingSheep(nums[i]))
    
        
