# Sorting Programs.

arr = [-2, 33, 4, 7, 1, 80, 9, 11, 13]


def bubble_sort(arr):
    size = len(arr)
    # it'll keep evaluating the rest of the list even though it's sorted.
    # we'll keep a boolean flag and check if any swaps were made in the previous iteration.
    # When no swaps are made, that means that the list is sorted
    has_swapped = True
    while(has_swapped):
        has_swapped = False
        for i in range(size - 1):
            for j in range(size - 1):
                if arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
                    has_swapped = True
    return arr


print("Bubble sort ... \n", bubble_sort(arr))

arr2 = [-2,33,4,7,1,80,9,11,13]

def selection_sort(arr2):
    size = len(arr)
    for i in range(size):
        for j in range(i, size):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


print("Selection sort ... \n", selection_sort(arr2))


# QUICK SORT

arr3 = [-2,-3,-1,5,4,-3,0]
arr4 = [1,2,3,4,5,6,7]

def quick_sort(arr):
    q_s(arr, 0, len(arr) - 1)

def q_s(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)
    q_s(arr, l, p - 1)
    q_s(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

quick_sort(arr3)
quick_sort(arr4)
print("Quick sort..\n", arr3)
print("Quick sort..\n", arr4)
