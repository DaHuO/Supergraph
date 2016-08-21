def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def find_median(arr,i,j,k):
    if arr[i] < arr[j]:
        if arr[i] < arr[k]:
            return j if arr[j] < arr[k] else k
        else:
            return i
    else:
        if arr[i] > arr[k]:
            return k if arr[j] < arr[k] else j
        else:
            return i

"""
quick1: quick sort using first element as pivot and swap pivot to the start
start: index of first element
end: index of last element
return: count of comparisons
"""
    
def quick1(arr,start,end):
    #print start,end
    if end <= start:
        return 0
    
    pivot = arr[start]
    #print "pivot is {}".format(pivot)
    i = start   #i : index of the last element in the part that less than pivot
    count = 0
    """
    if arr[j] < pivot:
    swap arr[j] to the end of the part that less than pivot
    i directs to the end of that part
    """
    for j in xrange(start,end+1):
        if arr[j] < pivot:
            swap(arr,i+1,j)
            i += 1
    # swap pivot to the middle        
    swap(arr,start,i)
    count = end - start
    count1 = quick1(arr,start,i-1)
    count2 = quick1(arr,i+1,end)
    count = count + count1 + count2
    return count

"""
quick2: quick sort using last element as pivot and swap pivot to the start
start: index of first element
end: index of last element
return: count of comparisons
"""
def quick2(arr,start,end):
    if end <= start:
        return 0
    
    swap(arr,start,end)         #swap last element to the start
    pivot = arr[start]
    i = start
    count = 0
    for j in xrange(start,end+1):
        if arr[j] < pivot:
            swap(arr,i+1,j)
            i += 1

    swap(arr,start,i)
    count = end - start
    count1 = quick2(arr,start,i-1)
    count2 = quick2(arr,i+1,end)
    count = count + count1 + count2
    return count

"""
quick3: quick sort using median element among (start,mid,end) as pivot
and swap pivot to the start
start: index of first element
end: index of last element
return: count of comparisons
"""    

def quick3(arr,start,end):
    if end <= start:
        return 0
    
    #print arr[start:end+1]
    mid = (start + end)/2           #index of the middle
    median = find_median(arr,start,mid,end) #find index of the median

    swap(arr,start,median)          #swap median to the start
    #print arr[start],arr[mid],arr[end]
    pivot = arr[start]
    #print pivot
    i = start
    count = 0
    for j in xrange(start,end+1):
        if arr[j] < pivot:
            swap(arr,i+1,j)
            i += 1

    swap(arr,start,i)
    count = end - start
    count1 = quick3(arr,start,i-1)
    count2 = quick3(arr,i+1,end)
    count = count + count1 + count2
    return count
    
        
if __name__ == "__main__":
##    testd = [3,2,6,4,5,7,9,1,8,0]
##    print quick3(testd,0,len(testd)-1)
##    print testd
    with open("QuickSort.txt","r") as f:
        data = [int(line) for line in f]
    #print "quick1 answer {}".format(quick1(data,0,len(data)-1))
    #print "quick2 answer {}".format(quick2(data,0,len(data)-1))
    print "quick3 answer {}".format(quick3(data,0,len(data)-1))
    

