import math
__author__ = 'pawel'
class Sorter:
    def merge_sort(self,array):
        if(len(array)>1):
            half = len(array)/2
            left = array[:half]
            right = array[half:]

            self.merge_sort(left)
            self.merge_sort(right)
            i=0;
            j=0;
            k=0;
            while i < len(left) and j < len(right):
                if(left[i]<right[j]):
                    array[k]=left[i]
                    i+=1
                else:
                    array[k]=right[j]
                    j+=1

                k+=1
            while i<len(left):
                array[k] = left[i]
                i+=1
                k+=1
            while j<len(right):
                array[k] = right[j]
                j+=1
                k+=1

    def bubble_sort_iteration(self,array):
        length = len(array)
        counter = 1;
        for i in range(length):
            for j in range(length-counter):
                if array[j]>array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
            counter+=1


    def check_sorting(self,array):
        for i in range(len(array)-1):
            if(array[i]>array[i+1]):
                return "incorrect"
        return "correct"

    def insertion_sort(self,array):
        for j in range (1,len(array)):
            key = array[j]
            i=j-1
            while i>=0 and array[i]>key:
                array[i+1]=array[i]
                i-=1
            array[i+1] = key

    def quicksort(self,array,first,last):
        if first < last :
            pivot=array[first]
            left = first+1
            right = last
            done = False
            while not done:
                while left <= right and array[left] < pivot :
                    left+=1
                while left <= right and array[right] > pivot :
                    right-=1
                if left > right:
                    done = True
                else :
                    array[left],array[right] = array[right],array[left]
            array[first],array[right]=array[right],array[first]
            self.quicksort(array,first,right-1)
            self.quicksort(array,right+1,last)

    def max_heap(self,array,i,length):
        left = 2*i
        right = 2*i+1
        if left <= length and  array[left-1] > array[i-1]:
            largestAt = left
        else:
            largestAt = i
        if right <= length and array[right-1] > array[largestAt-1]:
            largestAt = right
        if largestAt != i:
            array[i-1],array[largestAt-1] = array[largestAt-1],array[i-1]
            self.max_heap(array,largestAt,length)

    def heapsort(self,array):
        '''sorting using heapsort, nlogn, inline function, remember to use copy of array as attribute'''
        # create max heap
        for i in range(int(math.floor(len(array)/2)+1),0,-1):
            self.max_heap(array,i,len(array))
        #sort
        length = len(array)
        for i in range(len(array),1,-1):
            array[0],array[length-1]=array[length-1],array[0]
            length-=1
            self.max_heap(array,1,length)
