# masriadi sisfo b D0425309

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

data = [10, 20, 30, 40, 50]
print("Cari 30:", binary_search(data, 30))
