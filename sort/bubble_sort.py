table = [99, 43, 223, 12, 3, 0, -32, 2]

def bubble_sort(arr: list) -> list:
    arr_len = len(arr) - 1
    while arr_len:
        i = 0
        while i != arr_len:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        arr_len -= 1
    return arr

assert bubble_sort(table) == [-32, 0, 2, 3, 12, 43, 99, 223]
