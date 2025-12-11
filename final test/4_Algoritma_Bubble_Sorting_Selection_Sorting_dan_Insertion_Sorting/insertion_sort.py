# masriadi sisfo b D0425309

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

data = [50, 20, 40, 10, 30]
insertion_sort(data)
print("Insertion Sort:", data)

