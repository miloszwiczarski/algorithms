"""
Time complexiity O(n log n)
It requires the additiaonal space sa as input array
"""

table = [99, 43, 223, 12, 3, 0, -32, 2]

def merge_sort(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr
    
    arr1 = arr[:arr_len//2]
    arr2 = arr[arr_len//2:]
    print(arr1)
    print(arr2)

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)

def merge(arr1, arr2):
    arr3 = []

    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            arr3.append(arr2[0])
            arr2.pop(0)
        else:
            arr3.append(arr1[0])
            arr1.pop(0)
    
    while arr1:
        arr3.append(arr1[0])
        arr1.pop(0)

    while arr2:
        arr3.append(arr2[0])
        arr2.pop(0)
    
    return arr3


print(merge_sort(table))
