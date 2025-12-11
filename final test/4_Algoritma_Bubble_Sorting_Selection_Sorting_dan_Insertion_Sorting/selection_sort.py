# masriadi sisfo b D0425309

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

data = [50, 20, 40, 10, 30]
selection_sort(data)
print("Selection Sort:", data)
