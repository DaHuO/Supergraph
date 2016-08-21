# flip the first k+1 elements of an array
flipfunction = {'+':'-','-':'+'}
def flip(st,k):
    arr = list(st)
    i = 0
    j = k
    while i<=j:
        arr[i], arr[j] = flipfunction[arr[j]], flipfunction[arr[i]]
        i += 1
        j -= 1
    return ''.join(arr)

def stringNeighbors(st):
    result = []
    for k in range(len(st)):
        result.append(flip(st,k))
    return result

def stringBFS(st):
    goal = ''.join(['+']*len(st))
    if st == goal:
        return 0
    dist = {}
    dist[st] = 0
    visited = set()
    visited.add(st)
    queue = []
    queue.append(st)

    while True:
        cur = queue.pop(0)
        for nb in stringNeighbors(cur):
            if nb == goal:
                return dist[cur]+1
            elif nb not in visited:
                visited.add(nb)
                dist[nb] = dist[cur]+1
                queue.append(nb)

# main function
if __name__ == "__main__":
    T = int(input())
    nums = [0 for i in range(T)]

    # Take input
    for i in range(T):
        nums[i] = input()

    for i in range(T):
        print("Case #%d: " %(i+1) + str(stringBFS(nums[i])))
