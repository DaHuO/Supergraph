# Written in Python 3.5.1 by Kurtis Mackey


def sorter(myArray, smallsize=4):
    """Given an array of numbers, efficiently sorts the array
    using either mergesort on larger sized arrays or
    insertion sort on smaller arrays.

    Input:    An array of numbers
    Output:   A sorted array of numbers

    """
        
    def subsort(array, insertsize=smallsize):
        """Mergesort or Insertion Sort depending on array size"""
        if len(array) <= 1:
            return array
        elif len(array) <= insertsize:
            return insert_sort(array)
        else:
            mid = len(array) // 2
            return mergesort(subsort(array[:mid]), subsort(array[mid:]))

    def mergesort(left, right):
        """ Merging two sorted lists using Merge Sort

        Input:    Two sorted arrays
        Output:   A merged sorted array
        
        """
        #print('Starting Merge Sort on {0}'.format(array))
        merged_list = list()
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1
        merged_list.extend(left[i:])
        merged_list.extend(right[j:])
        return merged_list

    def insert_sort(array):
        """ A simple insertion sort algorithm

        Input:    An array of numbers
        Output:   A sorted array of numbers
        
        """
        #print('Starting Insert Sort on {0}'.format(array))
        for i in range(1, len(array)):
            j = i
            while j != 0 and array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
                j -= 1
        return array

    return subsort(myArray, insertsize=smallsize)



if __name__ == '__main__':
    
    from time import clock
    test = list(reversed(range(100)))
    def fastest_time(array):
        """Runs a number of tests to find the most efficient
        balance of insertion sort array size
        """
        fastest_time = 999999999999
        fastest_len = 0
        for i in range(2, len(test)):
            timer = 0
            testnum = 100
            for t in range(testnum):
                start = clock()
                sorter(test, i)
                stop = clock()
                timer += (stop-start)
            timer = (timer/testnum)*1000
            if timer < fastest_time:
                fastest_time = timer
                fastest_len = i
            print('Insert Sort on size {0} arrays took {1} time'.format(i, timer))
        print('Fastest was {0} with a time of {1}'.format(fastest_len, fastest_time))
    


