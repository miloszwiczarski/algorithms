table = [99, 43, 223, 12, 3, 0, -32, 2]

def selection_sort(arr: list) -> list:
    arr_len = len(arr) - 1
    while arr_len:
        i = 0
        big_index = 0
        while i < arr_len + 1:
            if arr[i] >= arr[big_index]:
                big_index = i
            i += 1
        arr[arr_len], arr[big_index] = arr[big_index], arr[arr_len]
        arr_len -= 1
    return arr

assert selection_sort(table) == [-32, 0, 2, 3, 12, 43, 99, 223]