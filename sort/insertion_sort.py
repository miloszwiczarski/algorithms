""" 
O(n^2) time complexity 

When array is in decreasing order 
we need to compare every single element
and that leads to n^2
"""

table = [99, 43, 223, 12, 3, 0, -32, 2]

def insertion_sort(arr: list) -> list:

    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1

    return arr





assert insertion_sort(table) == [-32, 0, 2, 3, 12, 43, 99, 223]