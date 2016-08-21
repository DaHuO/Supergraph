MAX_HEIGHT = 2500

def get_missing(heights):
    result = []
    for key in iter(heights):
        if (heights[key] % 2 == 1):
            result.append(key)
    return sorted(result)

def process(num):
    heights = {}
    for i in range(MAX_HEIGHT+1):
        heights[i] = 0
    for _ in range(num*2 -1):
        line = map(int, input().strip().split())
        for n in line:
            heights[n] += 1
    result = get_missing(heights)
    return (" ".join(map(str, result)))

if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        print("Case #" + str(case+1) + ": " + process(int(input())))

        
    
