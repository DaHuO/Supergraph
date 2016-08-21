import heapq

def heap_push(heap, item):
    idx = len(heap)
    heap.append(item)
    while idx:
        parent_idx = (idx-1) / 2
        if heap[parent_idx][0] < heap[idx][0]:
            tmp = heap[parent_idx]
            heap[parent_idx] = heap[idx]
            heap[idx] = tmp
        idx = parent_idx

def heapfy(heap, idx):
    sidx = len(heap)
    lidx = idx * 2 + 1
    ridx = idx * 2 + 2
    flag = -1
    if ridx < sidx and heap[ridx][0] > heap[lidx][0]:
        flag = 1 
    elif lidx < sidx:
        flag = 0

    if flag == 0 and heap[lidx][0] > heap[idx][0]:
        tmp = heap[idx]
        heap[idx] = heap[lidx]
        heap[lidx] = tmp
        heapfy(heap, lidx)
    if flag == 1 and heap[ridx][0] > heap[idx][0]:
        tmp = heap[idx]
        heap[idx] = heap[ridx]
        heap[ridx] = tmp
        heapfy(heap, ridx)

    return

def heap_pop(heap):
    res = heap[0]
    idx = len(heap)
    tmp = heap.pop()
    if heap:
        heap[0] = tmp
        heapfy(heap, 0)
    return res
    
if __name__ == '__main__':
    with open('A-large.in', 'r') as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            s = 0
            N = int(f.readline().strip())
            n = [ int(item) for item in f.readline().strip().split() ]
            h = []
            for i in xrange(N):
                item = [n[i], chr(i+ord('A'))]
                s += n[i]
                heap_push(h, item)
            #print h
            final_res = []
            while h:
                itemA = heap_pop(h)
                itemA[0] -= 1
                s -= 1
                res = [itemA[1]]
                if itemA[0]:
                    heap_push(h, itemA)
                if h and h[0][0] * 2 > s:
                    itemB = heap_pop(h)
                    s -= 1
                    itemB[0] -= 1
                    res.append(itemB[1])
                    if itemB[0]:
                        heap_push(h, itemB)
                    
                final_res.append(''.join(res))
            print "Case #%s: %s" % (t+1, ' '.join(final_res))




