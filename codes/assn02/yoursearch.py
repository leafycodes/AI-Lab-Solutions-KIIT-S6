def linear_search(list, key):
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1

def binary_search(list, key):
    low, high = 0, len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
