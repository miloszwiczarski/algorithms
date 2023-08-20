table = [1, 3, 4, 55, 65, 67, 69, 89, 122, 234, 434, 2322, 12233]


def binary_search_iterative(arr: list, find: int) -> bool:
    left = 0
    right = len(arr) - 1   
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == find:
            return True
        if arr[mid] > find:
            right = mid - 1            
        if arr[mid] < find:
            left = mid + 1
    return False 



def binary_search_recursive(arr: list, find: int) -> bool:
    left = 0
    right = len(arr) - 1
    return _binary_search_recursive_helper(arr, find, left, right)


def _binary_search_recursive_helper(arr: list, find: int, left: int, right: int) -> bool:
    if left >= right:
        return False

    mid = (left + right) // 2
    if arr[mid] == find:
        return True
    if arr[mid] > find:
        return _binary_search_recursive_helper(arr, find, left, mid - 1)            
    if arr[mid] < find:
        return _binary_search_recursive_helper(arr, find, mid + 1, right)    
    



if __name__ == '__main__':
    assert binary_search_iterative(table, 1) == True
    assert binary_search_iterative(table, 234) == True
    assert binary_search_iterative(table, 5000000) == False


    assert binary_search_recursive(table, 1) == True
    assert binary_search_iterative(table, 234) == True    
    assert binary_search_recursive(table, 5000000) == False
