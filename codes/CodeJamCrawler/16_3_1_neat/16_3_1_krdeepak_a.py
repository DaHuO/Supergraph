import sys
import os
import heapq

T = int(sys.stdin.readline().strip())

for t in range(T):
    n = int(sys.stdin.readline().strip())

    members = [int(x) for x in sys.stdin.readline().strip().split()]

    h = []
    count = 0
    for member in members:
        heapq.heappush(h, (-1*member, count))
        count += 1

    evac = []
    # print(h)

    #print(t)
    while len(h)>0:
        max1, ix1 = heapq.heappop(h)
        max2, ix2 = heapq.heappop(h)

        #print(ix1, ix2)


        if max1 == max2:
            if len(h) == 1:
                third, thirdx = heapq.heappop(h)
                #print('three', max1, max2, third)
                if max1 == third and third == -1:
                    #print('inside')
                    evac.append(chr(ix1+65))
                    heapq.heappush(h, (max2, ix2))
                    heapq.heappush(h, (third, thirdx))
                else:
                    evac.append(chr(ix1+65)+chr(ix2+65))
                    if max1+1<0:
                        heapq.heappush(h, (max1+1, ix1))
                    if max2+1<0:
                        heapq.heappush(h, (max2+1, ix2))
                    heapq.heappush(h, (third, thirdx))
            else:
                evac.append(chr(ix1+65)+chr(ix2+65))
                if max1+1<0:
                    heapq.heappush(h, (max1+1, ix1))
                if max2+1<0:
                    heapq.heappush(h, (max2+1, ix2))

        else:
            evac.append(chr(ix1+65)+chr(ix1+65))
            if max1+2<0:
                heapq.heappush(h, (max1+2, ix1))
            heapq.heappush(h, (max2, ix2))

        #print('h', h)
        #print(evac)

    sys.stdout.write('Case #{0}: {1}\n'.format(t+1, ' '.join(evac)))




