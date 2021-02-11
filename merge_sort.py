# Merge sort: recursive, divide and conquer procedure.
# merging is done in post order traversal.

arr = [1,4,2,-4,23,3,7,9,-2]

sorted_index = 0

# 2 Way merging, as we are merging two list here.
def merge(arr, l, mid, r):
    left_array = arr[l:mid + 1]
    right_array = arr[mid + 1:r + 1]
    i, j = 0, 0
    # Sorting wil start in the tree from right bottom left. so sorting index need to be at left and NOT 0.
    sorted_index = l  # (Its L not 1(one))
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[sorted_index] = left_array[i]
            i += 1
        else:
            arr[sorted_index] = right_array[j]
            j += 1
        sorted_index += 1

    while i < len(left_array):
        arr[sorted_index] = left_array[i]
        sorted_index += 1
        i += 1
    while j < len(right_array):
        arr[sorted_index] = right_array[j]
        sorted_index += 1
        j += 1


def merge_sort(arr, l, r):

    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)

merge_sort(arr, 0, len(arr) - 1)
print("merge sort ..\n", arr)
