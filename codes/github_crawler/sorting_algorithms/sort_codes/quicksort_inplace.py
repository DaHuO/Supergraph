import random

def partition(a, left, right, pivot):
    pivot_value = a[pivot]
    a[pivot], a[right] = a[right], a[pivot]
    store = left
    for i in range(left, right):
        if a[i] < pivot_value:
            a[i], a[store] = a[store], a[i]
            store += 1
    a[store], a[right] = a[right], a[store]
    return store

def quicksort(a, left, right):
    if left < right:
        pivot = random.randint(left, right)
        new_pivot = partition(a, left, right, pivot)
        quicksort(a, left, new_pivot - 1)
        quicksort(a, new_pivot + 1, right)

def main():
    a = [random.randint(1, 100) for i in range(1, 100)]
    print 'Start:', a
    quicksort(a, 0, len(a) - 1)
    print 'End:', a

if __name__ == '__main__':
    main()
