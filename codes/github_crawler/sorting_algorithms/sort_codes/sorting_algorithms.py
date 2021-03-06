def bubble_sort(file):
    """ Sorts a list of numbers using the bubble sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> bubble_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers

    """
    for j in range (len(file)): #Iterate through the entire list.
        swapped = True
        for i in range (len(file) - j - 1): #Iterate up the the outer index
            #Swap until the element being swapped meets it match
            if file[i] > file[i+1]:
                swapped = True
                file[i], file[i+1] = file[i+1], file[i]
        #If no swaps were made a whole loop, list is sorted
        if swapped == False:
            break
        
def selection_sort(file):
    """ Sorts a list of numbers using the selection sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> selection_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers

    """
    #Replace one element at a time with the next smallest value
    for outer in range (len(file)-1):
        for inner in range (outer, len(file)):
            if file[inner] < file[outer]:
                file[inner], file[outer] = file[outer], file[inner]

def insertion_sort(file):
    """ Sorts a list of numbers using the insertion sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> insertion_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
    file -- a list of numbers

    """
    #Swap current value with all values to the left until it is in place
    for outer in range(1, len(file)):
        current_pos = outer
        while file[current_pos] < file [current_pos - 1] and current_pos > 0:
            file[current_pos], file [current_pos -1] = (file[current_pos-1],
                                                        file[current_pos])
            current_pos += -1

def quick_sort(file):
    """ Sorts a list of numbers using the quicksort algorithm

    This implementation of quicksort does not sort in place, and instead
    returns a concatenation of several dynamically created lists. Thus,
    it may consume a prohibitive amount of memory for large lists.

    >>> file = [4,7,-9,8,0,1]
    >>> quick_sort(file)
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers

    Returns:
        A sorted list of numbers

    """
    #Base case
    if len(file) <= 1:
        return file
    #Pivot is halfway-ish value
    pivot = file[len(file)//2]
    small_pile = []
    large_pile = []
    pivot_count = 0
    #Group values according to their relationship to the pivot
    small_pile = [x for x in file if x < pivot]
    large_pile = [x for x in file if x > pivot]
    pivot_count = file.count(pivot)
    return(quick_sort(small_pile) +
           [pivot]*pivot_count +
           quick_sort(large_pile))

def quick_sort_inplace(file, lower = None, upper = None):
    """ Sorts a list of numbers using the quick sort algorithm, in place

    This implementation is more memory-efficient for large lists, as it
    sorts in place.

    >>> file = [4,7,-9,8,0,1]
    >>> quick_sort_inplace(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers
        Lower bound for the sort, default is zero
        Upper bound fot the sort, default is the last index of the list

    """
    #Set default values
    if lower is None : lower = 0
    if upper is None : upper = len(file) -1
    if upper-lower > 0:
        pivot_value = file[lower]
        l , h = lower, upper
        #Increment l and decrement h until file[l] is larger than the
        #pivot value and file[h] is smaller. A swap can then be made.
        #The pivot value can then be placed between the larger and
        #smaller values
        while h > l:
            while file[l] <= pivot_value and h > l:
                l += 1
            while file[h] > pivot_value and h >= l:
                h -= 1
            if h > l:
                file[l], file[h] = file[h], file[l]
        file[lower],file[h] = file[h],file[lower]
        #Recursively sort other subsections of the list
        quick_sort_inplace(file, lower, h-1)
        quick_sort_inplace(file, h+1, upper)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
